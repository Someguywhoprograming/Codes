import sys
import time
import random
import os
#from colorama import Fore, Style, init
from art import text2art
import math
import turtle
from turtle import *
from tkinter import Label, Tk, mainloop
from time import strftime
import winsound
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


#ha nem indul el akkor kell terminalba a :python system_app.py

# ========================
# FŐ ALKALMAZÁS
# ========================

class SystemApp:

    def __init__(self, root):
        self.root = root
        self.root.title("My System App")
        self.root.geometry("400x500")
        ####self.root.configure(bg="#1e1e1e")###########
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        self.canvas = tk.Canvas(self.root, bg="#000000", highlightthickness=0)
        self.canvas.place(relwidth=1, relheight=1)

        self.particles = []
        self.num_particles = 40
        self.connection_distance = 120


        for _ in range(self.num_particles):
            x = random.randint(0, width)
            y = random.randint(0, height)
            dx = random.uniform(-1, 1)
            dy = random.uniform(-1, 1)

            particle = {
                "x": x,
                "y": y,
                "dx": dx,
                "dy": dy,
                "id": self.canvas.create_oval(x, y, x+3, y+3, fill="cyan", outline="")
            }

            self.particles.append(particle)

        self.animate_particles()

        menu_frame = tk.Frame(self.canvas, bg="#000000")
        menu_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(menu_frame, text="MAIN MENU",
                 font=("Arial", 18, "bold"),
                 bg="#000000", fg="white").pack(pady=20)

        tk.Button(menu_frame, text="Calculator", width=20,
                  command=self.open_calculator).pack(pady=5)

        tk.Button(menu_frame, text="Games", width=20,
                  command=self.open_games_menu).pack(pady=5)

        tk.Button(menu_frame, text="Expense Tracker", width=20,
                  command=self.open_expense_tracker).pack(pady=5)

        tk.Button(menu_frame, text="Digital Clock", width=20,
                  command=self.open_clock).pack(pady=5)

        tk.Button(menu_frame, text="Text to Art", width=20,
                  command=self.open_art).pack(pady=5)

        tk.Button(menu_frame, text="Animation", width=20,
                  command=self.open_animation).pack(pady=5)
        
       


########################
       


    # ========================
    # CALCULATOR
    # ========================

    def open_calculator(self):
        win = tk.Toplevel(self.root)
        win.title("Calculator")
        win.geometry("300x350")

        entry = tk.Entry(win, font=("Arial", 18))
        entry.pack(pady=20)

        def calculate():
            try:
                result = eval(entry.get())
                entry.delete(0, tk.END)
                entry.insert(0, str(result))
            except:
                messagebox.showerror("Error", "Invalid expression")

        tk.Button(win, text="=", width=10,
                  command=calculate).pack(pady=10)

   
# ========================
# GAME MENU
# ========================

    def open_games_menu(self):

        win = tk.Toplevel(self.root)
        win.title("Game Menu")
        win.geometry("300x350")
        win.configure(bg="black")
    
        tk.Label(win,
                 text="🎮 GAME MENU 🎮",
                 font=("Arial", 16, "bold"),
                 bg="black",
                 fg="white").pack(pady=20)
    
        tk.Button(win,
                  text="Rock Paper Scissors",
                  width=20,
                  command=self.open_rps).pack(pady=5)
    
        #tk.Button(win,
        #          text="Guess The Number",
        #          width=20,
        #          command=self.open_guess_game).pack(pady=5)
    
        tk.Button(win,
                  text="2D Dodge Game",
                  width=20,
                  command=self.open_dodge_game).pack(pady=5)
    
        tk.Button(win,
                  text="Close",
                  width=20,
                  command=win.destroy).pack(pady=20)
        
# ========================
# 2D DODGE GAME
# ========================

    def open_dodge_game(self):

        game = tk.Toplevel(self.root)
        game.title("2D Dodge Game")
        game.geometry("400x600")
        game.resizable(False, False)

        canvas = tk.Canvas(game, width=400, height=600, bg="black")
        canvas.pack()

        player = canvas.create_rectangle(180, 550, 220, 590, fill="cyan")

        obstacles = []
        score = {"value": 0}
        speed = 5
        game_over = {"state": False}

        score_text = canvas.create_text(50, 20, fill="white",
                                         font=("Arial", 14),
                                         text="Score: 0")

        def move_left(event):
            if not game_over["state"]:
                canvas.move(player, -20, 0)

        def move_right(event):
            if not game_over["state"]:
                canvas.move(player, 20, 0)

        game.bind("<Left>", move_left)
        game.bind("<Right>", move_right)

        def create_obstacle():
            if not game_over["state"]:
                x = random.randint(0, 360)
                obstacle = canvas.create_rectangle(x, 0, x+40, 40, fill="red")
                obstacles.append(obstacle)
                game.after(1000, create_obstacle)

        def move_obstacles():
            if not game_over["state"]:
                for obs in obstacles:
                    canvas.move(obs, 0, speed)

                    if check_collision(obs):
                        end_game()

                score["value"] += 1
                canvas.itemconfig(score_text,
                                  text=f"Score: {score['value']}")

                game.after(50, move_obstacles)

        def check_collision(obs):
            player_coords = canvas.coords(player)
            obs_coords = canvas.coords(obs)

            return not (player_coords[2] < obs_coords[0] or
                        player_coords[0] > obs_coords[2] or
                        player_coords[3] < obs_coords[1] or
                        player_coords[1] > obs_coords[3])

        def end_game():
            game_over["state"] = True
            canvas.create_text(200, 300,
                               text="GAME OVER",
                               fill="white",
                               font=("Arial", 24, "bold"))

        create_obstacle()
        move_obstacles()
        game.focus_set()


    # ========================
    # ROCK PAPER SCISSORS
    # ========================

    def open_rps(self):
        win = tk.Toplevel(self.root)
        win.title("Rock Paper Scissors")
        win.geometry("300x300")
        result_label = tk.Label(win, text="", font=("Arial", 12))
        result_label.pack(pady=20)
        def play(choice):
            options = ["rock", "paper", "scissor"]
            computer = random.choice(options)
            if choice == computer:
                result = "Tie!"
            elif (choice == "rock" and computer == "scissor") or \
                 (choice == "paper" and computer == "rock") or \
                 (choice == "scissor" and computer == "paper"):
                result = "You Win!"
            else:
                result = "You Lose!"
            result_label.config(
                text=f"You: {choice}\nComputer: {computer}\n{result}"
            )
        for opt in ["rock", "paper", "scissor"]:
            tk.Button(win, text=opt.capitalize(),
                      command=lambda o=opt: play(o)).pack(pady=5)

    # ========================
    # EXPENSE TRACKER
    # ========================

    def open_expense_tracker(self):
        win = tk.Toplevel(self.root)
        win.title("Expense Tracker")
        win.geometry("350x450")

        tk.Label(win, text="Description").pack()
        entry_desc = tk.Entry(win)
        entry_desc.pack()

        tk.Label(win, text="Amount").pack()
        entry_amt = tk.Entry(win)
        entry_amt.pack()

        listbox = tk.Listbox(win)
        listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        total_label = tk.Label(win, text="Total: $0.00",
                               font=("Arial", 12, "bold"))
        total_label.pack()

        filename = "expenses.txt"

        def update_total():
            total = 0
            for item in listbox.get(0, tk.END):
                total += float(item.split("$")[1])
            total_label.config(text=f"Total: ${total:.2f}")

        def save_data():
            with open(filename, "w") as f:
                for item in listbox.get(0, tk.END):
                    f.write(item + "\n")

        def load_data():
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    for line in f:
                        listbox.insert(tk.END, line.strip())
                update_total()

        def add_expense():
            desc = entry_desc.get()
            amt = entry_amt.get()

            if desc and amt:
                try:
                    value = float(amt)
                    listbox.insert(tk.END, f"{desc}: ${value:.2f}")
                    entry_desc.delete(0, tk.END)
                    entry_amt.delete(0, tk.END)
                    update_total()
                    save_data()
                except:
                    messagebox.showerror("Error", "Amount must be a number")
            else:
                messagebox.showwarning("Warning", "Fill all fields")

        tk.Button(win, text="Add Expense",
                  command=add_expense).pack(pady=5)

        load_data()

    # ========================
    # DIGITAL CLOCK
    # ========================

    def open_clock(self):
        win = tk.Toplevel(self.root)
        win.title("Digital Clock")
        win.geometry("300x200")

        clock_label = tk.Label(win, font=("Arial", 30),
                               bg="black", fg="lime")
        clock_label.pack(fill="both", expand=True)

        def update_time():
            clock_label.config(text=strftime("%H:%M:%S"))
            clock_label.after(1000, update_time)

        update_time()

    # ========================
    # TEXT TO ART
    # ========================

    def open_art(self):

        win = tk.Toplevel(self.root)
        win.title("Text to Art")
        win.geometry("700x500")

        tk.Label(win, text="Enter text",
                 font=("Arial", 12)).pack(pady=5)
        
        entery = tk.Entry(win, width=40, font=("Arial", 14))
        entery.pack(pady=5)

        output_box = tk.Text(win, height=20, width=80,
                             bg="black", fg="lime",
                             font=("Courier", 10))
        output_box.pack(pady=10)

        def generate_art():
            text = entery.get()
            if text:
                ascii_art = text2art(text)
                output_box.delete("1.0", tk.END)
                output_box.insert(tk.END, ascii_art)
            else:
                messagebox.showwarning("Warning", "Please enter text")

        tk.Button(win, text="Generate",
              command=generate_art).pack(pady=5)

        
    # ========================
    # ANIMATION
    # ========================

    def open_animation(self):

        selector = tk.Toplevel(self.root)
        selector.title("Select Animation")
        selector.geometry("300x250")

        tk.Label(selector, text="Choose Animation",
                font=("Arial", 14, "bold")).pack(pady=20)

        def run_heart():
            selector.destroy()
            self.animation_heart()

        def run_covid():
            selector.destroy()
            self.animation_covid()

        def run_atoms():
            selector.destroy()
            self.animation_atoms()

        def run_star():
            selector.destroy()
            self.animation_star()

        tk.Button(selector, text="Heart",
                width=20, command=run_heart).pack(pady=5)

        tk.Button(selector, text="Covid Spiral",
                width=20, command=run_covid).pack(pady=5)

        tk.Button(selector, text="Atoms",
                width=20, command=run_atoms).pack(pady=5)
        tk.Button(selector, text="Star Field",
                width=20, command=run_star).pack(pady=5)
        
    def animation_heart(self):
        turtle.reset()
        turtle.bgcolor("black")
        turtle.color("red")
        turtle.speed(0)

        def hearta(k):
             return 15*math.sin(k)**3
        def heartb(k):
            return 12*math.cos(k)-5*\
            math.cos(2*k)-2*\
            math.cos(3*k)-\
            math.cos(4*k)
        speed(0)
        bgcolor('black')
        for i in range(6000):
            goto(hearta(i)*20, heartb(i)*20)
            for j in range(5):
                color("red")
            goto(0,0)
        done()

    def animation_covid(self):
        color('green')
        bgcolor('black')
        speed(11)
        hideturtle()
        b = 0
        while  b < 200:
            right(b)
            forward(b * 3) 
            b = b + 1  


    def animation_atoms(self):
        bgcolor("black")
        tracer(0)
        drawer = Turtle()
        drawer.hideturtle()
        drawer.speed(0)
        drawer.width(1)
        num_nodes = 50
        node_size = 0.5
        connection_distacne = 120
        move_speed = 0.8 
        nodes = []
        for _ in range(num_nodes):
            node = Turtle()
            node.shape("circle")
            node.color("cyan")
            node.penup()   
            x = random.randint(-300, 300)
            y = random.randint(-200, 200)
            node.goto(x, y)
            dx = random.uniform(-move_speed, move_speed)
            dy = random.uniform(-move_speed, move_speed)
            nodes.append({'turtle': node, 'dx': dx, 'dy': dy})
                    
        while True:
            drawer.clear()
            for i in range(len(nodes)):
                for j in range(i + 1, len(nodes)):
                    pos1 = nodes[i]['turtle'].pos()
                    pos2 = nodes[j]['turtle'].pos()
                    distance = nodes [i]['turtle'].distance(nodes[j]['turtle'])
                    if distance < connection_distacne:
                        opacity = 1 - (
                            distance / connection_distacne)
                        gray_value = int(100 * opacity)
                        drawer.color(gray_value / 100.0,
                            gray_value / 100.0,
                            gray_value / 100.0)
                        drawer.penup()
                        drawer.goto(pos1)
                        drawer.pendown()
                        drawer.goto(pos2)
            for node_data in nodes:
                t = node_data['turtle']
                x, y = t.pos()
                new_x = x + node_data['dx']
                new_y = y + node_data['dy']
                if not (
        -window_width() / 2 < new_x  < window_width () / 2 ):
                    node_data['dx'] *= -1
                if not (
        -window_height() / 2 < new_y < window_height () /2):
                    node_data['dy'] *= -1
                t.goto(new_x, new_y)
            update()

#######################
    def animate_particles(self):

        self.canvas.delete("line")

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        for p in self.particles:
            p["x"] += p["dx"]
            p["y"] += p["dy"]

            if p["x"] <= 0 or p["x"] >= width:
                p["dx"] *= -1
            if p["y"] <= 0 or p["y"] >= height:
                p["dy"] *= -1

            self.canvas.coords(p["id"],
                               p["x"], p["y"],
                               p["x"]+3, p["y"]+3)

        for i in range(len(self.particles)):
            for j in range(i+1, len(self.particles)):

                p1 = self.particles[i]
                p2 = self.particles[j]

                dist = ((p1["x"] - p2["x"])**2 +
                        (p1["y"] - p2["y"])**2) ** 0.5

                if dist < self.connection_distance:

                    opacity = 1 - dist / self.connection_distance
                    color = f"#00{int(255*opacity):02x}{int(255*opacity):02x}"

                    self.canvas.create_line(
                        p1["x"], p1["y"],
                        p2["x"], p2["y"],
                        fill=color,
                        tags="line"
                    )

        self.root.after(30, self.animate_particles)      

##################
# Stars
########

    def animation_star(self):

                win = tk.Toplevel(self.root)
                win.title("Circular Star Field")
                win.attributes("-fullscreen", True)

                win.update()

                width = win.winfo_screenwidth()
                height = win.winfo_screenheight()

                canvas = tk.Canvas(win, width=width, height=height, bg="black")
                canvas.pack(fill="both", expand=True)

                center_x = width // 2
                center_y = height // 2

                stars = []

                # ⭐ CSILLAGOK LÉTREHOZÁSA
                for _ in range(500):
                    radius = random.uniform(50, min(center_x, center_y)-20)
                    angle = random.uniform(0, 2*math.pi)
                    speed = random.uniform(0.005, 0.03)
                    size = random.uniform(2, 4)

                    brightness = random.randint(100, 255)
                    fade_dir = random.choice([-3, 3])

                    star_id = canvas.create_oval(0, 0, 0, 0, outline="")

                    stars.append({
                        "radius": radius,
                        "angle": angle,
                        "speed": speed,
                        "size": size,
                        "brightness": brightness,
                        "fade_dir": fade_dir,
                        "id": star_id
                    })

                # ⭐ ANIMÁCIÓ
                def animate():
                    for star in stars:
                    
                        # Mozgás
                        star["angle"] += star["speed"]

                        x = center_x + star["radius"] * math.cos(star["angle"])
                        y = center_y + star["radius"] * math.sin(star["angle"])
                        r = star["size"]

                        canvas.coords(star["id"], x-r, y-r, x+r, y+r)

                        # Smooth fade
                        star["brightness"] += star["fade_dir"]

                        if star["brightness"] >= 255 or star["brightness"] <= 80:
                            star["fade_dir"] *= -1

                        b = star["brightness"]
                        color = f"#{b:02x}{b:02x}{b:02x}"
                        canvas.itemconfig(star["id"], fill=color)

                    win.after(30, animate)

                win.bind("<Escape>", lambda e: win.destroy())

                animate()
    

# ========================
# PROGRAM INDÍTÁS
# ========================

#if __name__ == "__main__":
#    root = tk.Tk()
#    app = SystemApp(root)
#    root.mainloop()

if __name__ == "__main__":

    def start_main_app():
        splash.destroy()
        root = tk.Tk()
        SystemApp(root)
        root.mainloop()

    splash = tk.Tk()
    splash.title("Loading...")
    splash.configure(bg="#000000")

    # Teljes képernyő
    splash.attributes("-fullscreen", True)

    width = splash.winfo_screenwidth()
    height = splash.winfo_screenheight()

    title_label = tk.Label(
        splash,
        text="First App",
        font=("Arial", 50, "bold"),
        bg="#000000",
        fg="white"
    )
    title_label.pack(pady=height // 3)

    from tkinter import ttk
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TProgressbar",
        thickness=40,
        troughcolor="#000000",
        background="#2EA300"
    )

    progress = ttk.Progressbar(
        splash,
        orient="horizontal",
        length=width // 2,
        mode="determinate"
    )
    progress.pack()

    splash.update()

    def loading():
        for i in range(101):
            progress["value"] = i
            splash.update_idletasks()
            time.sleep(0.1)
        start_main_app()

    splash.after(100, loading)
    splash.mainloop()


