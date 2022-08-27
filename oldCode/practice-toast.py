import emoji
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification

app = ttk.Window()

toast = ToastNotification(
    title="标题",
    message="弹窗消息",
    duration=5000,
    bootstyle='light',
    alert=True,
    icon='💡',
    position=[100, 100, 'se']
)
toast.show_toast()

for k, v in emoji.EMOJI_UNICODE.items():
    print(v, end=' ')

app.mainloop()
