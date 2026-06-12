from art import text2art
import math
import turtle
from turtle import *
from tkinter import Label, Tk, mainloop
from time import strftime
import time
import winsound
import random
import tkinter as tk
from tkinter import messagebox




mail = "WELCOME"

for betu in mail:
    print(betu, end="", flush=True)
    winsound.Beep(1000, 100)
    time.sleep(0.1)

print()

print("Loading", end="")
for i in range(5):
    time.sleep(1)
    print(".", end="")


def logo():
    logo = r"""
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""
    print(logo)
    

logo()



def menu():
    print("------- Main Menu ---------")
    print("-----1. - Calculator ------")
    print("-----2. - Animation -------")
    print("-----3. - Time ------------")
    print("-----4. - Animet Text -----")
    print("-----5. - Game ------------")
    print("-----6. Expense Tracker----")
         


while True:
    menu()
    answer = input("Option?")

    if answer == "1":
        print(eval(input("Enter expression: ")))
   

   
   
    if answer == "2":
        optinon = input("What shall I do?")



        if optinon == "heart":
                def hearta(k):
                    return 15*math.sin(k)**3
                def heartb(k):
                    return 12*math.cos(k)-5*\
                    math.cos(2*k)-2*\
                    math.cos(3*k)-\
                    math.cos(4*k)
                speed(0)
                bgcolor("black")
                for i in range(6000):
                    goto(hearta(i)*20, heartb(i)*20)
                    for j in range(5):
                        color("red")
                    goto(0,0)
                done()



        if optinon == "covid":
            color('green')
            bgcolor('black')
            speed(11)
            hideturtle()
            b = 0
            while  b < 200:
                right(b)
                forward(b * 3) 
                b = b + 1       

        if optinon == "atoms":
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


    if answer == "3":
        window = Tk()
        window.title("Digital Clock")

        def time():
            mytime = strftime("%H:%M:%S")
            clock.config(text = mytime)
            clock.after(1000, time)

        clock = Label(window,
                      font = ("arial", 48, "bold"),
                      background= "black",
                      foreground= "white")
        clock.pack(anchor= "center")
        time()
    
    if answer == "4":

        text = input("Enter your text:")
        art = text2art(text)
        print(art)

    if answer == "5":

        optinon = ("rock", "paper", "scissor" )
        runniung = True

        while runniung:
            player = None
            computer = random.choice(optinon)

            while player not in optinon:
                player = input("Select an option (rock, paper. scissor) : ").lower()
                
            print(f"Player : {player}")
            print(f"Computer : {computer}")

            if player == computer:
                print("It's a tie")
            elif player == "rock" and computer == "scissor":
                print("You win")
            elif player == "paper" and computer == "rock":
                print("You win")
            elif player == "scissor" and computer == "paper":
                print("You win")
            
            else:
                print("You lose")

            run = input("Enter 'q' to quit and any other key to continue : ").lower

            if run == "q":
                    break

        print("Thanks for playing")

    if answer == "6":
        def save_data():
            with open("expenses.text", "w") as f:
                for item in listbox.get(0, tk.END):
                    f.write(item + "\n")

        def load_data():
            try:
                with open("expenses.text", "r") as f:
                    for line in f:
                        if line.strip():
                            listbox.insert(tk.END, line.strip())


                    if listbox.size() > 0:
                        current_total = sum(float(i.split(
                            '$')[1]) for i in listbox.get(
                                0, tk.END))
                        label_total.config(
                            text=f"Total: $ {current_total:.2f}")
            except FileNotFoundError:
                pass

        def add_expense(event=None):
            desc = entery_desc.get()
            amt = entery_amt.get()

            if desc and amt:
                try:
                    value = float(amt)
                    listbox.insert(
                        tk.END, f"{desc}: ${value:.2f}")
                    entery_desc.delete(0, tk.END)
                    entery_amt.delete(0, tk.END)

                    current_total = sum(float(i.split('$')[1]
                            ) for i in listbox.get(0, tk.END))
                    label_total.config(
                        text=f"Total: ${current_total:.2f}")
                    
                    save_data()
                    entery_desc.focus_set()
                except ValueError:
                    messagebox.showerror("Error",
                            "Amount must be a number")
                else:
                    messagebox.showwarning("Warning", 
                                        "Fill all fields")
                    
        root = tk.Tk()
        root.title("Pocket Tracker")
        root.geometry("300x450")

        tk.Label(root, text="Description").pack(pady=5)
        entery_desc = tk.Entry(root)
        entery_desc.pack(pady=5)

        tk.Label(root, text="Amount ($)").pack(pady=5)
        entery_amt = tk.Entry(root)
        entery_amt.pack(pady=5)

        tk.Button(root,
                text="Add Expense",
                command=add_expense).pack(pady=10)

        listbox = tk.Listbox(root)
        listbox.pack(pady=10, fill=tk.BOTH, expand=True,
                    padx=20)

        label_total = tk.Label(root,
                            text="Total: $0.00",
                            font=("Arial", 12, "bold"))
        label_total.pack(pady=10)

        root.bind('<Return>', add_expense)

        load_data()

        root.mainloop()
            