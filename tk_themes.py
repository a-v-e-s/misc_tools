import os
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.tk.call('lappend', 'auto_path', './awthemes-10.4.0')
        for themefile in os.listdir('awthemes-10.4.0'):
            if themefile.endswith('.tcl'):
                try:
                    self.tk.call('package', 'require', themefile[:-4])
                except tk.TclError:
                    pass

        self.title('Theme Demo')
        self.geometry('400x300')
        self.style = ttk.Style(self)

        self.root = ttk.Frame(self)
        self.root.pack()
        label = ttk.Label(self.root, text='Name:')
        label.grid(column=0, row=0, padx=10, pady=10, sticky='w')
        textbox = ttk.Entry(self.root)
        textbox.grid(column=1, row=0, padx=10, pady=10, sticky='w')
        btn = ttk.Button(self.root, text='Show')
        btn.grid(column=2, row=0, padx=10, pady=10, sticky='w')

        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self.root, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme
            )
            rb.pack(expand=True, fill='both')

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())


if __name__ == '__main__':
    app = App()
    app.mainloop()
