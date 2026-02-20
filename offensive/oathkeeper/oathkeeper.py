import tkinter as tk
import random
import time
import pyautogui 

## TO DO: refactor to ps? or bat? or c? --> then add in the walking and images with the popups, also add in image popups for random things + start making a key wonky

class DesktopCat:
    def __init__(self):
        self.window = tk.Tk()
        
        self.img_idle = tk.PhotoImage(file='offensive/images/front.png')
        self.walk_right = tk.PhotoImage(file='offensive/images/left.png')
        self.walk_left = tk.PhotoImage(file='offensive/images/right.png')
        
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)        
        self.dialects = [
            "Meow!",   
            "Add me on Linkedin: https://www.linkedin.com/in/rheasharma-cs/",   
            "Chococat reigns supreme!",       
            "Feed me a Monster please...",
            "I really hate the goldfish from Terraria."    
            "Find me if you can :3",
            "let me download your malware on my computer 🥺"
        ]
        
        screen_w = self.window.winfo_screenwidth()
        screen_h = self.window.winfo_screenheight()
        self.x, self.y = screen_w - 275, screen_h - 440 
        
        self.speech_bubble = tk.Label(self.window, bg='white', fg='black', font=('agave', 14, 'bold'), wraplength=200)
        self.label = tk.Label(self.window, bd=0, bg='black', image=self.img_idle)
        self.label.pack(side='bottom')
        
        self.state = "talking" 
        self.last_switch_time = time.time()
        self.current_dialect = random.choice(self.dialects)

        self.update_behavior()
        self.window.mainloop()

    def update_behavior(self):
        current_time = time.time()
        
        if current_time - self.last_switch_time > 60:
            self.switch_to_new_state()

        if self.state == "walking":
            self.speech_bubble.pack_forget() 
            self.walk_logic()
        
        elif self.state == "talking":
            self.talk_logic()
            
        elif self.state == "snatch":
            self.speech_bubble.pack_forget() 
            self.snatch_logic()

        self.window.after(20, self.update_behavior)

    def switch_to_new_state(self, force_state=None):
        self.last_switch_time = time.time()
        self.state = force_state if force_state else random.choice(["walking", "talking", "snatch"])
        self.current_dialect = random.choice(self.dialects)

    def walk_logic(self):
        self.x += 2
        if self.x > (self.window.winfo_screenwidth() - 100): 
            self.switch_to_new_state(force_state="talking")
            return 

        self.label.configure(image=self.walk_right)
        self.window.geometry(f'+{self.x}+{self.y}')

    def talk_logic(self):
        self.label.configure(image=self.img_idle)
        self.speech_bubble.configure(text=self.current_dialect)
        if not self.speech_bubble.winfo_ismapped():
            self.speech_bubble.pack(side='top', fill='x')
        
        self.window.geometry(f'+{self.x}+{self.y}')

    def snatch_logic(self):
        self.x += 3
        if self.x > (self.window.winfo_screenwidth() - 100): 
            self.switch_to_new_state(force_state="talking")
            return

        self.label.configure(image=self.walk_right)
        self.window.geometry(f'+{self.x}+{self.y}')
        pyautogui.moveTo(self.x + 50, self.y + 50) 
        
        if time.time() - self.last_switch_time > 10:
            self.state = "walking"

if __name__ == "__main__":
    DesktopCat()