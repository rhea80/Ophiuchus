import tkinter as tk
import random
import math
import time
import ctypes
from PIL import Image, ImageTk

class DesktopCat:
    def __init__(self):
        self.window = tk.Tk()
        self.window.overrideredirect(True)
        self.window.attributes("-topmost", True)
        self.window.config(bg="black")
        self.window.wm_attributes("-transparentcolor", "black")

        self.load_gif("offensive/oathkeeper/assets/images/chococatfinal.gif")

        self.bubble_width = 240
        self.bubble_padding = 14
        self.side_margin = 20

        self.cat_w = self.frames[0].width()
        self.cat_h = self.frames[0].height()

        self.w = self.cat_w + self.bubble_width + self.side_margin * 3
        self.h = max(self.cat_h + 40, 170)

        self.canvas = tk.Canvas(self.window, width=self.w, height=self.h,
                                bg="black", highlightthickness=0)
        self.canvas.pack()

        self.cat_x = self.side_margin + self.cat_w // 2
        self.cat_y = self.h - self.cat_h // 2

        self.cat = self.canvas.create_image(self.cat_x, self.cat_y,
                                            image=self.frames[0])

        self.dialects = [
            "Meow!",
            "Add me on Linkedin: https://www.linkedin.com/in/rheasharma-cs/",
            "I <3 Chococat",
            "Feed me a Monster please...",
            "I really hate the goldfish from Terraria.",
            "Find me if you can :3",
            "let me download your malware on my computer :pleading_face:",
            "this is so epic swag!?", 
            ":3",
            "Anyone wanna play Marvel Rivals?"
        ]

        self.bubble_text = self.canvas.create_text(
            self.cat_w + self.side_margin * 2 + self.bubble_width // 2,
            70,
            text=random.choice(self.dialects),
            fill="#000000",
            font=("Arial", 12, "bold"),
            width=self.bubble_width
        )

        self.bubble_bg = self.canvas.create_polygon(
            0, 0, 0, 0,
            fill="white",
            outline="black",
            width=2
        )

        self.update_bubble_shape()
        self.canvas.tag_raise(self.bubble_text)

        self.screen_w = self.window.winfo_screenwidth()
        self.screen_h = self.window.winfo_screenheight()

        self.x = random.randint(0, self.screen_w - self.w)
        self.y = random.randint(0, self.screen_h - self.h)

        self.speed = 7
        self.hostage = False
        self.next_pounce_allowed = 0

        self.animate_gif()
        self.follow_cursor()
        self.update_speech()

        self.window.mainloop()

    def load_gif(self, path):
        self.frames = []
        self.delays = []
        gif = Image.open(path)
        try:
            while True:
                frame = gif.copy().convert("RGBA")
                self.frames.append(ImageTk.PhotoImage(frame))
                self.delays.append(gif.info.get("duration", 80))
                gif.seek(len(self.frames))
        except EOFError:
            pass
        self.frame_index = 0

    def animate_gif(self):
        self.canvas.itemconfig(self.cat, image=self.frames[self.frame_index])
        delay = self.delays[self.frame_index]
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.window.after(delay, self.animate_gif)

    def follow_cursor(self):
        if not self.hostage:
            mouse_x = self.window.winfo_pointerx()
            mouse_y = self.window.winfo_pointery()

            dx = mouse_x - self.x
            dy = mouse_y - self.y
            distance = math.hypot(dx, dy)

            if distance < 40 and time.time() >= self.next_pounce_allowed:
                self.pounce()
                return

            if distance > 1:
                dx /= distance
                dy /= distance
                self.x += dx * self.speed
                self.y += dy * self.speed

            self.window.geometry(f"+{int(self.x)}+{int(self.y)}")

        self.window.after(16, self.follow_cursor)

    def pounce(self):
        self.hostage = True
        self.capture_end_time = time.time() + 100
        self.next_pounce_allowed = time.time() + 300
        self.hold_cursor()

    def hold_cursor(self):
        if time.time() < self.capture_end_time:
            center_x = int(self.x + self.cat_w // 2)
            center_y = int(self.y + self.cat_h // 2)
            ctypes.windll.user32.SetCursorPos(center_x, center_y)
            self.window.after(10, self.hold_cursor)
        else:
            self.hostage = False

    def update_speech(self):
        new_text = random.choice(self.dialects)
        self.canvas.itemconfig(self.bubble_text, text=new_text)
        self.update_bubble_shape()
        self.window.after(600000, self.update_speech)

    def update_bubble_shape(self):
        bbox = self.canvas.bbox(self.bubble_text)
        x1, y1, x2, y2 = bbox
        x1 -= self.bubble_padding
        y1 -= self.bubble_padding
        x2 += self.bubble_padding
        y2 += self.bubble_padding
        tail_y = (y1 + y2) // 2
        points = [
            x1, y1,
            x2, y1,
            x2, y2,
            x1, y2,
            x1, tail_y + 10,
            self.cat_x + self.cat_w // 2 - 10, self.cat_y - 20,
            x1, tail_y - 10
        ]
        self.canvas.coords(self.bubble_bg, points)
        self.canvas.tag_lower(self.bubble_bg, self.bubble_text)


if __name__ == "__main__":
    DesktopCat()