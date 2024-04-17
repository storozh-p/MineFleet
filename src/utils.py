def start_minecraft(nickname, password, selected_server, servers_list):
    if selected_server in servers_list:
        print(selected_server)
    else:
        print("Not found")
