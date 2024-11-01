from playwright.sync_api import expect
import time


class AlertHandler:
    def __init__(self, page):
        self.page = page
        self.dialog_message = None
        self.page.once('dialog', self.handle_dialog)

    def handle_dialog(self, dialog):
        self.dialog_message = dialog.message
        dialog.accept()

    def verify_dialog_message(self, message):
        assert self.dialog_message == message