import tkinter as tk
import tkinter.ttk as ttk


class MineFleetGUI:
    def __init__(self, root: tk.Tk, server_list):
        self.root = root
        self.servers = server_list

        self.root.geometry("300x130")
        self.root.title("MineFleet")

        self.password_input_text = ttk.Label(self.root, text="Enter nickname:")
        self.password_input_text.grid(row=0, column=0, padx=5, pady=5)
        self.password_input = ttk.Entry(self.root)
        self.password_input.grid(row=0, column=1, padx=5, pady=5)

        self.password_input_text = ttk.Label(self.root, text="Enter password:")
        self.password_input_text.grid(row=1, column=0, padx=5, pady=5)
        self.password_input = ttk.Entry(self.root, show="*")
        self.password_input.grid(row=1, column=1, padx=5, pady=5)

        self.server_selector_text = ttk.Label(self.root, text="Select server:")
        self.server_selector_text.grid(row=2, column=0, padx=5, pady=5)
        self.server_selector = ttk.Combobox(self.root, values=[i for i in self.servers])
        self.server_selector.grid(row=2, column=1, padx=5, pady=5)

        self.play_btn = ttk.Button(self.root, text="Play!")
        self.play_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.root.mainloop()
