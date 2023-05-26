
import flet as ft

from home import Home



async def main(page: ft.page):
    page.window_min_width = 350
    page.window_min_height = 750
    page.title = "ProSkill"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme_seed="indigo")
    page.theme_mode = ft.ThemeMode.LIGHT
    #page.scroll = "auto"
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    Home(),
                ],
            )
        )
        def go_store(e):
            page.route = "/store"
            page.update()
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
   # await page.add_async(Home())



ft.app(target=main)
