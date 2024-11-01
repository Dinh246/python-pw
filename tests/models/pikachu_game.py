import re
from playwright.sync_api import expect


class Pikachu:
    def __init__(self, page):
        self.page = page
        self.player_name_textbox = page.locator("[id=playerName]")
        self.player_info = page.locator("[id=playerInfo]")
        self.grid_boxes = page.locator("[id=grid] .outer")
        self.start_game_button = page.get_by_role(
            "button", name="Bắt đầu chơi")

    def get_all_unique_grids(self):
        return set(grid.inner_text() for grid in self.grid_boxes.all())

    def select_same_grids(self, num):
        grids = self.grid_boxes.filter(has_text=num)
        for grid in grids.all():
            grid.click(delay=500)
