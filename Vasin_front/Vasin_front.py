
import flet as ft

from home import Home


async def main(page: ft.page):
    page.window_min_width = 350
    page.window_min_height = 750
    page.title = "ProSkill"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme_seed="indigo")
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "auto"
    await page.add_async(Home())



ft.app(target=main)