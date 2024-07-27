import flet as ft
import atexit
import library.parsers.fashiongirl


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = 'Shafa Bot v2'
        self.page.window.width = 720
        self.page.window.height = 600
        self.page.window.resizable = True
        self.page.window.center()
        self.page.window.full_screen = False
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.selected = {}
        self.accountsSelected = {}
        self.initdownloadselected = None

        atexit.register(self.quit)

    def quit(self):
        self.page.window_destroy()


def run():
    ft.app(App)


if __name__ == '__main__':
    run()
