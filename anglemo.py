import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=200, height=400)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

for x in range(0,35):
    canvas.move(1,10,0)       # 삼각형을 화면 수평으로 이동시 x(가로) 값은 양수 y(세로)값은 0
    tk.update()
    time.sleep(0.05)

for x in range(0,14):
    canvas.move(1,0,10)      # 아래로 움직이기 가로값 0 세로값 10 
    tk.update()
    time.sleep(0.05)


for x in range(0,35):
    canvas.move(1,-10,0)    # 뒤로 움직이기 가로값(-10) 
    tk.update()
    time.sleep(0.05)

for x in range(0,14):         # 아래에서 위로 세로값 (-10)
    canvas.move(1,0,-10)
    tk.update()
    time.sleep(0.05)
