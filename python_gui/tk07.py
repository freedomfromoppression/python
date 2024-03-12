from tkinter import *

app = Tk()
entry = Entry(app)
entry.grid(row=0, column=0)
btn = Button(app, text='생성')
btn.grid(row=0, column=1)
txt = Text(app)
txt.grid(row=1, column=0, columnspan=2)
app.mainloop()
# 수량을 입력받아 Text 위젯에 입력받은 수량만큼 로또번호 출력
# 1. button event
# 2. entry value
# 3. lotto 생성
# 생성 수량만큼 Text insert
