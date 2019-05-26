import sys,random

def init_maze(tate, yoko):
    #リストの初期化
    #外周と内部の一つ飛ばしの壁の設定
    l=[]
    for i in range(tate):
        m=[]
        for j in range(yoko):
            if i==0 or i==tate-1 or j==0 or j== yoko-1:#外周は１
                m.append(1)
            elif i%2==0 and j%2==0:
                m.append(1)
            else:
                m.append(0)
        l.append(m)
    return l

def make_maze(tate=9, yoko=9):
    maze = init_maze(tate,yoko)
    tate=len(maze)
    yoko=len(maze[0])

    #input_your_code

    maze[1][1]=10#スタートは10(左上)
    maze[tate-2][yoko-2]=11#ゴールは11(右下)
    return maze

if __name__=="__main__":
    maze=make_maze()
    for i in maze:
        print(i)
