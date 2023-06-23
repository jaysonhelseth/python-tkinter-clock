from tkinter import *
from tkinter import ttk
from tkinter import font
from datetime import datetime

class Main(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Clock")
        self.geometry("300x300")
        self.font_color = "#ffd454"
        self.attributes("-fullscreen", 1)

        self.content = Frame(self, background="black")
        
        self.time_value = StringVar()
        self.time_font = font.Font(self.content, font="TkFixedFont", size=12)
        self.time = Label(self.content, text="00:00", bg="black", fg=self.font_color, font=self.time_font, textvariable=self.time_value)
        
        self.extra_value = StringVar()
        self.extra_font = font.Font(self.content, font="TkFixedFont", size=12)
        self.extra = Label(self.content, text="Tue PM", bg="black", fg=self.font_color, font=self.extra_font, textvariable=self.extra_value)

        self.content.grid(row=0, column=0, sticky=(N, S, E, W))
        self.time.grid(row=0, column=0, sticky=(N, S, E, W))
        self.extra.grid(row=1, column=0, sticky=(S))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(0, weight=1)

        self.time_format = "%I:%M"
        self.extra_format = "%a %p"
        self.tick_ms = 500

        self.on_tick()
        self.bind('<Configure>', self.on_resize)
        self.after(self.tick_ms, self.on_tick)
        self.mainloop()

    def on_resize(self, event):
        self.redraw_text()

    def on_tick(self):
        # self.redraw_text()

        now = datetime.now()
        self.time_value.set(now.strftime(self.time_format))
        self.extra_value.set(now.strftime(self.extra_format))

        self.after(self.tick_ms, self.on_tick)

    def redraw_text(self):
        w = self.winfo_width()

        self.time_font['size'] = int(w / 4)
        self.extra_font['size'] = int(w / 20) 
        

if __name__ == "__main__":
    app = Main()