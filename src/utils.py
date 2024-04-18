import os.path
import subprocess
import zipfile

import minecraft_launcher_lib.command
import mysql.connector
import requests

import config as cfg
import tkinter as tk


def print_debug(text):
    if cfg.debug_mode:
        print(text)


def download_client(server, minecraft_dir):
    if not os.path.exists(minecraft_dir):
        os.mkdir(minecraft_dir)

        response = requests.get(url=cfg.servers[server]["url"])

        try:
            with open(f"{minecraft_dir}\\{server}.zip", "wb") as file:
                file.write(response.content)
        except Exception as error:
            print_debug(error)
        finally:
            with zipfile.ZipFile(f"{minecraft_dir}\\{server}.zip", "r") as archive:
                archive.extractall(minecraft_dir)
            os.remove(f"{minecraft_dir}\\{server}.zip")
    else:
        print_debug("Client downloaded!")


def start_minecraft(root: tk.Tk, nickname, password, selected_server, servers_list):
    if selected_server in servers_list:
        if nickname != "" and password != "":
            try:
                connection = mysql.connector.connect(
                    host=cfg.db_host,
                    user=cfg.db_user,
                    password=cfg.db_pass,
                    database=cfg.db_name
                )

                if connection.is_connected():
                    print_debug("Connected to MariaDB database")

                    cursor = connection.cursor()

                    query = f"SELECT * FROM {cfg.user_table} WHERE nickname = %s"
                    cursor.execute(query, (nickname,))

                    user = cursor.fetchone()

                    if user:
                        if password == user[2]:
                            try:
                                print_debug("Downloading")
                                download_client(server=selected_server, minecraft_dir=f"{cfg.minecraft_dir}\\{selected_server}")
                            except Exception as error:
                                print_debug(error)
                            finally:
                                options = {
                                    "nickname": nickname,
                                    "uuid": "",
                                    "token": ""
                                }

                                root.destroy()
                                subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=cfg.servers[selected_server]["version"], minecraft_directory=f"{cfg.minecraft_dir}\\{selected_server}", options=options))

                        else:
                            print_debug("Password incorrect!")
                    else:
                        print_debug("User not found!")

            except mysql.connector.Error as error:
                print_debug(f"Error while connecting to MariaDB: {error}")

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print_debug("MariaDB connection closed")
        else:
            print_debug("Enter username and password!")
    else:
        print_debug("Not found")
