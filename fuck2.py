from turtle import *
import random

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
