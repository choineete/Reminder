from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
image = Image.open("../remind.ico")
icon('test', image, menu=menu(
    item(
        'With submenu',
        menu(
            item(
                'Show message',
                lambda icon, item: icon.notify('Hello World!')),
            item(
                'Submenu item 2',
                lambda icon, item: icon.remove_notification()))))).run()