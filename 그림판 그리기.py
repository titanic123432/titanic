from tkinter import *

pen_color = "black" #펜 색상
pen_size = 2 #펜 사이즈
shape_size = 10 #도형 크기
my_tool = "pen" #현재 선택된 도구
fill_color = "white"# 도형의 색상

# 캔버스에 그림 그리는 함수
def paint(event):
    global pen_size
    x1, y1 = event.x, event.y
    x2, y2 = event.x + pen_size, event.y + pen_size
    canvas.create_line(x1, y1, x2, y2, width = pen_size, fill = pen_color)

# 펜 색깔 변경 함수
def change_color(color) :
    global pen_color
    pen_color = color
    
# 펜 크기 변경 함수
def change_size(btn) :
    global pen_size
    if btn == "plus" :
        pen_size += 1
    else :
        if pen_size > 2 :
            pen_size -= 1

# 캔버스 초기화하는 함수
def clear_canvas() :
    canvas.delete("all")

w = 6

win = Tk()
win.title("My paint")
win.geometry("500x500+200+200")
canvas     = Canvas(win, width = 510, height = 470, bg = "white")
canvas.bind("<B1-Motion>", paint)# 마우스 왼쪽 버튼을 누르면서 움직일 때
canvas.bind("<Double-Button-1>", draw_shape)

#색상 변경 버튼
btn_white  = Button(win, text = "white", bg = "white", width = w, command = lambda : change_color("white"))
btn_black  = Button(win, text = "black", bg = "black", fg = "white", width = w, command = lambda : change_color("black"))
btn_blue   = Button(win, text = "blue", bg = "blue",  fg = "white", width = w, command = lambda : change_color("blue"))
btn_green  = Button(win, text = "green", bg = "green",  fg = "white", width = w, command = lambda : change_color("green"))
btn_yellow = Button(win, text = "yellow", bg = "yellow", width = w, command = lambda : change_color("yellow"))
btn_red    = Button(win, text = "red", bg = "red",  fg = "white", width = w, command = lambda : change_color("red"))


# 도구 변경 버튼
btn_canvas = Button(win, text = "canvas\ncolor", bg = "white", fg = "black",width = w, height = h, command = lambda :change_tool("canvas"))
btn_pen = Button(win, text = "pen\ncolor", bg = "black", fg = "white",width = w, height = h, command = lambda :change_tool("pen"))
btn_fill = Button(win, text = "fill\ncolor", bg = "white", fg = "black",width = w, height = h, command = lambda :change_tool("shape"))

#도형 변경 버튼
btn_oval = Button(win, text = "○",bg = "white", width = w, height = h, command = lambda:chamge_tool("oval"))
btn_rect = Button(win, text = "□",bg = "white", width = w, height = h, command = lambda:chamge_tool("rect"))
btn_tri = Button(win, text = "△",bg = "white", width = w, height = h, command = lambda:chamge_tool("tri"))

btn_plus   = Button(win, text = "+", bg = "white", width = w, command = lambda : change_size("plus"))
btn_minus  = Button(win, text = "-", bg = "white", width = w, command = lambda : change_size("minus"))

btn_clear  = Button(win, text = "clear", bg = "white", width = w, command = clear_canvas)

canvas.grid(row = 0, column = 0, columnspan = 6)
btn_canvas.grid(row = 1, column = 0)
btn_black.grid(row = 1, column = 1)
btn_blue.grid(row = 1, column = 2)
btn_green.grid(row = 1, column = 3)
btn_plus.grid(row = 1, column = 4)
btn_pen.grid(row = 2, column = 0)
btn_white.grid(row = 2, column = 1)
btn_red.grid(row = 2, column = 2)
btn_.yellow(row = 2, column = 3)
btn_.minus(row = 2, column = 4)

btn_fill.grid(row = 3, column = 0)
btn_oval.grid(row = 3, column = 1)
btn_rect.grid(row = 3, column = 2)
btn_tri.grid(row = 3, column = 3)
btn_clear.grid(row = 3, column = 4)


win.mainloop()
