import mysql.connector
import config as cfg
import tkinter as tk


def print_debug(text):
    if cfg.debug_mode:
        print(text)


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
                            root.destroy()
                            print_debug("Game starting")
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
