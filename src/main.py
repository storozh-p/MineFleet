import tkinter as tk
from gui import MineFleetGUI


class MineFleet:
    def __init__(self):
        # Global settings
        self.servers = {
            "HiTech": {}
        }

        # GUI
        self.root = tk.Tk()
        MineFleetGUI(root=self.root, server_list=self.servers)


if __name__ == "__main__":
    MineFleet()
