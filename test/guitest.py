import tkinter as  tk

win = tk.Tk()
win.title("C语言中文网")


# 将图片放在主窗口的右边
lab =tk.Label(win).pack(side="right")

# 显示文字，设置文本格式
text = "C语言中文网欢迎您,\n"\
       "这里有精彩的教程,\n "\
       "这里有数不尽的知识宝藏"
lab_text =tk.Label(win,text=text,fg ='#7CCD7C',font=('微软雅黑',15,'italic'),justify='left',padx=10).pack(side='left')
win.mainloop()