
import flet as ft

from home import Home


def main(page: ft.page):
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
                   ft.Stack(
            [
                ft.Row(
                    [
                    ft.Image(
                        f"https://github.com/VasinIgor96/New-Project/blob/master/Fonnn.jpg?raw=true", 
                        fit=ft.ImageFit.FILL
                    ),
                    ],
                  
                  ),
                 ft.Container(
                    margin = ft.margin.only(top = 175),
                    alignment=ft.alignment.center,
                    content=ft.Card(
                        content=ft.Container(
                            
                            height=400,
                            width=400,
                            padding=25,
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [ft.Text("Реєстрація",weight=ft.FontWeight.BOLD, size=20)],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ), 

                                     ft.Row(
                                        [ft.TextField(label="І'мя", prefix_icon=ft.icons.PERSON)],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ), 
                                       
                                      ft.Row(
                                        [ft.TextField(label="Email", prefix_icon=ft.icons.EMAIL)],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ), 
                              
                                       ft.Row(
                                        [ft.TextField(label="Пароль", password=True, can_reveal_password=True, prefix_icon=ft.icons.LOCK)],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),

                                       ft.Row(
                                        [ft.Checkbox(label="Я погоджуюсь з умовами обробки\n персональних данних", value=False, fill_color=ft.colors.BLUE_900)],
                                        
                                    ),

                                    ft.Row(
                                        [ft.ElevatedButton("Далі", width=120, style=ft.ButtonStyle (ft.colors.BLUE_900, side=ft.BorderSide(2, ft.colors.BLUE_900)), on_click=lambda _: page.go("/store"))],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            ),
                           
                        )
                    ),
                 ),
             
            ],
        )
                ],
            )
        )

        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [

                        #ft.AppBar(title=ft.Text("Вихід"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Розпочати тест", on_click=lambda _: page.go("/")),
                    ],
                    ft.Row(
                        [ft.ElevatedButton("Вихід", width=120, style=ft.ButtonStyle (ft.colors.BLUE_900, side=ft.BorderSide(2, ft.colors.BLUE_900)))],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND
                          )   
                    ),
                  
                ),
                               
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)




ft.app(target=main)
