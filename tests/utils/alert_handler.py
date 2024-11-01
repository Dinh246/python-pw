from playwright.sync_api import expect
import time


class AlertHandler:
    def __init__(self, page):
        self.page = page
        self.dialog_message = None

    def accept_dialog(self):
        dialog_message = None

        def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        return dialog_message
