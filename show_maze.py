from tkinter import *
from maze1 import *

tile_size=20

#迷路の表示(正方形の表示)
def draw_maze(cv, data):
    rows=len(data)
    cols=len(data[0])

    for y in range(rows):
        #１マスのサイズ指定
        y1 = y*tile_size
        y2 = y1+tile_size
        for x in range(cols):
            #１マスのサイズ指定
            x1 = x*tile_size
            x2 = x1+tile_size
            p=data[x][y]
            #色の指定
            if p==0:    color="white"#通路
            if 1<=p<=9: color="#404040"#壁
            if p==10:   color="red"
            if p==11:   color="blue"
            #正方形を書く
            cv.create_rectangle(
            x1, y1, x2, y2, #座標
            fill=color, #色
            outline="black",width=2#枠線
            )

def create_window(data):
    win=Tk()
    win.title("迷路")
    rows=len(data)
    cols=len(data[0])
    cv=Canvas(win,
        width=(cols*tile_size),
        height=(rows*tile_size))
    cv.pack()
    draw_maze(cv, data)
    win.mainloop()

if __name__=="__main__":
    import sys
    try:
        tate=int(sys.argv[1])
        yoko=int(sys.argv[2])
        if tate%2==0:
            print("偶数を奇数に直します(tate)")
            tate+=1
        if yoko%2==0:
            print("偶数を奇数に直します(yoko)")
            yoko+=1
        maze=make_maze(tate, yoko)
        create_window(maze)
    except:
        maze=make_maze()
        create_window(maze)
