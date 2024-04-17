import tkinter as tk
import config as cfg
from gui import MineFleetGUI


class MineFleet:
    def __init__(self):
        # GUI
        self.root = tk.Tk()
        MineFleetGUI(root=self.root, server_list=cfg.servers)


if __name__ == "__main__":
    MineFleet()
