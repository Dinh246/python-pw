import re
from playwright.sync_api import Page, expect
from models.pikachu_game import Pikachu
from utils.alert_handler import AlertHandler
import asyncio


def test_pikachu_game(page: Page):
    page.goto("https://material.playwrightvn.com/games/002-pikachu.html")
    pikachu_page = Pikachu(page)
    handler = AlertHandler(page)

    # Expect title game pikachu display
    expect(page).to_have_title("Game Pikachu chơi tự động bằng Playwright")

    # Expect textbox input player info display
    expect(pikachu_page.player_name_textbox).to_be_visible()

    # Enter player info & click start
    pikachu_page.player_name_textbox.fill("Dinh246")
    pikachu_page.start_game_button.click()

    # Expect game start
    expect(pikachu_page.player_info).to_be_visible()
    expect(pikachu_page.grid_boxes.first).to_be_visible()

    # Handle alert after finished
    dialog_message = None

    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()

    page.once("dialog", handle_dialog)

    # Start matching same grids
    all_unique_nums = pikachu_page.get_all_unique_grids()
    for num in all_unique_nums:
        pikachu_page.select_same_grids(num)

    for grid in pikachu_page.grid_boxes.all():
        expect(grid).to_have_class(re.compile(r"fade-out"))
    assert dialog_message == "Bạn đã thắng cuộc!"
