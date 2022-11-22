import tkinter as tk
from client.gui_app import Frame,barraDeMenu


def main():
    root = tk.Tk()
    barraDeMenu(root=root)
    app = Frame(root= root)

    root.mainloop()



if __name__ == '__main__':
    main()