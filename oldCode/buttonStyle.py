# -*- coding:utf-8 -*-
from tkinter import *


class buttons:
    def __init__(self):
        root = Tk()
        root.title("按钮")  # 设置窗口标题
        root.geometry("600x600")  # 设置窗口大小 注意：是x 不是*
        '''按钮样式'''
        # 按钮文字切换
        self.btsd = Label(root, text='按钮文字切换：')
        self.bts = Button(root, text='按钮开始', command=self.Button_text_switch)
        # 按钮状态
        self.button_state = Label(root, text='按钮状态：')
        self.disabled_state = Button(root, text='禁用状态')
        self.disabled_state.config(state=DISABLED)
        self.usual_status = Button(root, text='普通状态')
        self.usual_status.config(state=NORMAL)
        self.active = Button(root, text='活跃状态')
        self.active.config(state=ACTIVE)
        # 鼠标点击到按钮后改变颜色，activebackground='背景色'，activeforeground='前景色'
        self.mouse_click_color = Label(root, text='鼠标点击颜色：')
        self.click_background_colour = Button(root, text='背景色', activebackground='blue')
        self.click_foreground_colour = Button(root, text='前景色', activeforeground='blue')
        # 按钮边框大小，bd='边框大小'
        self.button_border_size = Label(root, text='按钮边框大小：')
        self.border = Button(root, text='按钮边框', bd=5)
        # 按钮颜色，bg='背景色', fg='前景色'
        self.the_button_color = Label(root, text='按钮颜色：')
        self.button_background_colour = Button(root, text='背景色', bg='blue')
        self.button_foreground_colour = Button(root, text='前景色', fg='blue')
        # 按钮字体格式， font=('字体', 字体大小, 'bold/italic/underline/overstrike')
        self.button_font_format = Label(root, text='按钮字体格式：')
        self.button_face1 = Button(root, text='软体雅黑/12/重打印', font=('软体雅黑', 10, 'overstrike'))
        self.button_face2 = Button(root, text='宋体/12/斜体', font=('宋体', 10, 'italic'))
        self.button_face3 = Button(root, text='黑体/12/加粗', font=('黑体', 10, 'bold'))
        self.button_face4 = Button(root, text='楷体/12/下划线', font=('楷体', 10, 'underline'))
        # 按钮高度，height='高度'
        self.button_border_xy = Label(root, text='按钮边xy：')
        self.button_height = Button(root, text='按钮高度', height=2)
        self.button_width = Button(root, text='按钮宽度', width=16)
        # 按钮图片设置，image=图片变量。图片必须以变量的形式赋值给image，图片必须是gif格式。
        self.button_image_settings = Label(root, text='按钮图片设置：')
        gif = PhotoImage(file="img.png")
        self.button_image = Button(root, image=gif)
        # 按钮文字对齐方式，可选项包括LEFT, RIGHT, CENTER
        self.text_alignment = Label(root, text='文字对齐方式：')
        self.text_left = Button(root, text='左对齐\n文字左侧对齐', justify=LEFT)
        self.text_center = Button(root, text='居中对齐\n文字居中对齐', justify=CENTER)
        self.text_tight = Button(root, text='右对齐\n文字右侧对齐', justify=RIGHT)
        # 按钮文字与边框之间的间距，padx='x轴方向间距大小'，pady='y轴间距大小'
        self.text_border_spacing = Label(root, text='文字边框间距：')
        self.button_padx = Button(root, text='x轴间距', padx=0)
        self.button_pady = Button(root, text='y轴间距', pady=10)
        # 框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。
        self.box_style = Label(root, text='按钮框样式：')
        self.button_relief1 = Button(root, text='边框平坦', relief=FLAT)
        self.button_relief2 = Button(root, text='边框凹陷', relief=SUNKEN)
        self.button_relief3 = Button(root, text='边框凸起', relief=RAISED)
        self.button_relief4 = Button(root, text='边框压线', relief=GROOVE)
        self.button_relief5 = Button(root, text='边框脊线', relief=RIDGE)
        # 按钮达到限制字符后换行显示
        self.Line_shows_state = Label(root, text='文字换行显示：')
        self.selfLine_shows = Button(root, text='1234567890', wraplength=30)
        # 下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，第两个字符带下划线，以此类推
        self.underline_state = Label(root, text='文字标下划线：')
        self.underline = Button(root, text='12345', underline=2)

        '''grid布局'''
        self.btsd.grid(row=1, column=1, sticky='E')
        self.bts.grid(row=1, column=2, sticky='NW')
        self.button_state.grid(row=2, column=1, sticky='E')
        self.disabled_state.grid(row=2, column=2, sticky='NW')
        self.usual_status.grid(row=2, column=3, sticky='NW')
        self.active.grid(row=2, column=4, sticky='NW')
        self.mouse_click_color.grid(row=3, column=1, sticky='E')
        self.click_background_colour.grid(row=3, column=2, sticky='NW')
        self.click_foreground_colour.grid(row=3, column=3, sticky='NW')
        self.button_border_size.grid(row=4, column=1, sticky='E')
        self.border.grid(row=4, column=2, columnspan=3, sticky='NW')
        self.the_button_color.grid(row=5, column=1, sticky='E')
        self.button_background_colour.grid(row=5, column=2, sticky='NW')
        self.button_foreground_colour.grid(row=5, column=3, sticky='NW')
        self.button_font_format.grid(row=6, column=1, sticky='E')
        self.button_face1.grid(row=6, column=2, columnspan=2, sticky='NW')
        self.button_face2.grid(row=6, column=4, columnspan=2, sticky='NW')
        self.button_face3.grid(row=6, column=6, columnspan=2, sticky='NW')
        self.button_face4.grid(row=6, column=8, columnspan=2, sticky='NW')
        self.button_border_xy.grid(row=7, column=1, sticky='E')
        self.button_height.grid(row=7, column=2, sticky='NW')
        self.button_width.grid(row=7, column=3, columnspan=2, sticky='NW')
        self.button_image_settings.grid(row=8, column=1, sticky='E')
        self.button_image.grid(row=8, column=2, columnspan=3, sticky='NW')
        self.text_alignment.grid(row=9, column=1, sticky='E')
        self.text_left.grid(row=9, column=2, columnspan=2, sticky='NW')
        self.text_center.grid(row=9, column=4, columnspan=2, sticky='NW')
        self.text_tight.grid(row=9, column=6, columnspan=2, sticky='NW')
        self.text_border_spacing.grid(row=10, column=1, sticky='E')
        self.button_padx.grid(row=10, column=2, sticky='NW')
        self.button_pady.grid(row=10, column=3, sticky='NW')
        self.box_style.grid(row=11, column=1, sticky='E')
        self.button_relief1.grid(row=11, column=2, sticky='NW')
        self.button_relief2.grid(row=11, column=3, sticky='NW')
        self.button_relief3.grid(row=11, column=4, sticky='NW')
        self.button_relief4.grid(row=11, column=5, sticky='NW')
        self.button_relief5.grid(row=11, column=6, sticky='NW')
        self.Line_shows_state.grid(row=12, column=1, sticky='E')
        self.selfLine_shows.grid(row=12, column=2, sticky='NW')
        self.underline_state.grid(row=13, column=1, sticky='E')
        self.underline.grid(row=13, column=2, sticky='NW')
        root.mainloop()

    # 按钮开关设置
    def Button_text_switch(self):
        if self.bts['text'] == '按钮开始':  # 如果文字是开始，则改为关闭
            self.bts['text'] = '按钮关闭'
            print('按钮开始')
        else:  # 如果不是开始，则改为开始
            self.bts['text'] = '按钮开始'
            print('按钮关闭')


if __name__ == '__main__':
    buttons()