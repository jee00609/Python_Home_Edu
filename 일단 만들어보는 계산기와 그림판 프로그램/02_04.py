from tkinter import *

##변수##
window = None
canvas = None

#함수

##메인코드##
window = Tk()
window.title("그림판 비슷한 프로그램")
canvas = Canvas(window,height=300,width=300)
canvas.pack()
window.mainloop()
