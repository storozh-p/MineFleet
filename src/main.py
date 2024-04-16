import tkinter as tk
import tkinter.ttk as ttk


class MineFleet:
    def __init__(self):
        # Global settings
        self.servers = {
            "HiTech": {}
        }

        # GUI
        self.root = tk.Tk()
        self.root.geometry("300x100")
        self.root.title("MineFleet")

        self.username_input_text = ttk.Label(self.root, text="Enter nickname:")
        self.username_input_text.grid(row=0, column=0, padx=5, pady=5)
        self.username_input = ttk.Entry(self.root)
        self.username_input.grid(row=0, column=1, padx=5, pady=5)

        self.server_selector_text = ttk.Label(self.root, text="Select server:")
        self.server_selector_text.grid(row=1, column=0, padx=5, pady=5)
        self.server_selector = ttk.Combobox(self.root, values=[i for i in self.servers])
        self.server_selector.grid(row=1, column=1, padx=5, pady=5)

        self.play_btn = ttk.Button(self.root, text="Play!")
        self.play_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.root.mainloop()


if __name__ == "__main__":
    MineFleet()
