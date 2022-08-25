import ttkbootstrap as ttk
import tkinter as tk
'''

style = Style(theme='yeti')

window = style.master
ttk.Button(window, text="Submit", style='success.TButton').pack(side='left', padx=5, pady=10)
ttk.Button(window, text="Submit", style='success.Outline.TButton').pack(side='left', padx=5, pady=10)
window.mainloop()
'''

'''
# 创建主要窗体
root_windows = tk.Tk()
# 为主窗口命名
root_windows.title('测试')
# 设置窗口宽高
root_windows.geometry('450x300')
# 更改左上角窗口图标
root_windows.iconbitmap('remind.ico')
# 设置主窗口背景颜色，英文单词 or 16进制 or 颜色常量
root_windows["background"] = "#FFFFFC"
# 添加文本内，设置字体的前景色和背景色，和字体类型、字体
text = tk.Label(root_windows, text='Hello World', bg="#FFFFFC", fg="#000000", font=('Times', 16, 'bold italic'))
# 将文本内容至于主窗体内
text.pack()
# 添加按钮，以及按钮的文本，并通过command参数设置关闭窗口的功能
button = tk.Button(root_windows, text="关闭", command=root_windows.quit())
# 将按钮置入主窗口内
button.pack(side="bottom")
# 开启主循环
root_windows.mainloop()
'''

''' 美化界面
from ttkbootstrap.constants import *
root = ttk.Window()

root.iconbitmap('remind.ico')

b1 = ttk.Button(root, text="Solid Button", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Outline Button", bootstyle=(SUCCESS, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()

'''

'''
from ttkbootstrap.constants import *

root = ttk.Window(themename='yeti')
root.geometry("450x300")

for color in root.style.colors:
    b = ttk.Button(root, text=color, bootstyle=color)
    b.pack(side=LEFT, padx=5, pady=5)
root.mainloop()
'''



'''
b1 = ttk.Button(root, text='primary', bootstyle=PRIMARY)
b1.pack(side=LEFT, padx=5, pady=5)

b2 = ttk.Button(root, text='secondary', bootstyle=SECONDARY)
b2.pack(side=LEFT, padx=5, pady=5)

b3 = ttk.Button(root, text='dark', bootstyle=DARK)
b3.pack(side=RIGHT, padx=5, pady=5)

b4 = ttk.Button(root, text='light', bootstyle=LIGHT)
b4.pack(side=RIGHT, padx=5, pady=5)


root.mainloop()
'''