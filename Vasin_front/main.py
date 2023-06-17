
import flet as ft

from home import Home


def main(page: ft.page):
    def page_resize(e):
        pw.update()
    page.on_resize = page_resize
    pw = ft.Text(bottom=350, right=150, style="displaySmall")
    page.overlay.append(pw)
    page.window_min_width = 400
    page.window_min_height = 750
    page.title = "ProSkill"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme_seed="indigo")
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "auto"

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
                                margin=ft.margin.only(top=175),
                                alignment=ft.alignment.center,
                                content=ft.Card(
                                    content=ft.Container(
                                        height=440,
                                        width=400,
                                        padding=25,
                                        content=ft.Column(
                                            [


                                                ft.Row(
                                                    [
                                                        ft.Text("Реєстрація", weight=ft.FontWeight.BOLD, size=20)
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),

                                                ft.Row(
                                                    [
                                                        ft.TextField(label="І'мя", prefix_icon=ft.icons.PERSON)
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),

                                                ft.Row(
                                                    [
                                                        ft.TextField(label="Email", prefix_icon=ft.icons.EMAIL)
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),

                                                ft.Row(
                                                    [
                                                        ft.TextField(label="Пароль", password=True,can_reveal_password=True,prefix_icon=ft.icons.LOCK)
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),

                                                ft.Row(
                                                    [
                                                        ft.Checkbox(label="Я погоджуюсь з умовами обробки \n персональних даних",value=False, fill_color=ft.colors.INDIGO_500)
                                                    ],
                                                ),

                                                ft.Row(
                                                    [
                                                        ft.OutlinedButton("Продовжити", width=280,style=ft.ButtonStyle(ft.colors.INDIGO_500,side=ft.BorderSide(1,ft.colors.BLACK)),on_click=lambda _: page.go("/store"))
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),

                                                ft.Row(
                                                    [
                                                        ft.TextButton("Я вже маю аккаунт!",on_click=lambda _: page.go("/login"))
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER
                                                ), 
                                            ]
                                        ),
                                    ),
                                ),
                            ),
                        ]
                    ),
                ]
            )
        ),



        if  page.route == "/login":
            page.views.append(
                ft.View(
                      "/login",
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
                                    margin=ft.margin.only(top=175),
                                    alignment=ft.alignment.center,
                                    content=ft.Card(
                                        content=ft.Container(
                                            height=350,
                                            width=400,
                                            padding=30,
                                            content=ft.Column(
                                                [

                                                    ft.Row(
                                                        [
                                                            ft.Text("Вхід в обліковий запис", weight=ft.FontWeight.BOLD, size=20)
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                    ),

                                                    ft.Row(
                                                        [
                                                            ft.TextField(label="Email", prefix_icon=ft.icons.EMAIL)
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                    ),

                                                    ft.Row(
                                                        [
                                                            ft.TextField(label="Пароль", password=True,can_reveal_password=True,prefix_icon=ft.icons.LOCK)
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                    ),

                                                    ft.Row(
                                                        [
                                                            ft.Checkbox(label="Я погоджуюсь з умовами обробки \n персональних даних",value=False, fill_color=ft.colors.INDIGO_500)
                                                        ],
                                                    ),

                                                    ft.Row(
                                                        [
                                                            ft.OutlinedButton("Продовжити", width=280,style=ft.ButtonStyle(ft.colors.INDIGO_500,side=ft.BorderSide(1,ft.colors.BLACK)),on_click=lambda _: page.go("/store"))
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                    ),
                                                ]                   
                                            ),
                                        ),
                                    ),
                                ),
                            ]
                        ),
                    ]
                )
            ),

        if  page.route == "/store":
            page.views.append(
                ft.View(
                      "/store",
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

                                ft.Row(
                                    [
                                        ft.IconButton(icon=ft.icons.OUTPUT_OUTLINED, width=80, style=ft.ButtonStyle(color={
                                        ft.MaterialState.HOVERED: ft.colors.WHITE,
                                        ft.MaterialState.DEFAULT: ft.colors.INDIGO_500,
                                        }), icon_size=40, tooltip= "Вихід",  on_click=lambda _: page.go("/"))
                                    ],
                                        alignment=ft.MainAxisAlignment.END
                                ),
                                            
                                ft.Container(
                                    margin=ft.margin.only(top=45),
                                    alignment=ft.alignment.center,
                                    content=ft.Card(
                                        content=ft.Container(
                                            border_radius=15,
                                            height=600,
                                            width=1300,
                                            padding=25,
                                            bgcolor=ft.colors.INDIGO_100,
                                            content=ft.Column(
                                                [
                                                    
                                                    ft.Row(
                                                        [
                                                            ft.Text("Ласкаво просимо до тесту на професійну орієнтацію!", weight=ft.FontWeight.BOLD, color='indigo900', size=35)
                                                        ],
                                                         alignment=ft.MainAxisAlignment.CENTER,
                                                    ), 
                                                
                                                    ft.Row(
                                                        [
                                                            ft.Text("Цей тест розроблений для допомоги вам у визначенні вашої професійної спрямованості та вибору кар'єрного шляху, який може найкраще підійти саме вам.\nТест складається з ряду запитань які допоможуть виявити ваші інтереси, навички, особисті якості та цінності.\nВам буде запропоновано різні ситуації, вибори та питання, на які потрібно відповісти чесно та уважно.\nПам'ятайте, що немає правильних або неправильних відповідей - важливо висловити свої власні думки та переконання.\nБудь ласка, перед початком тесту забезпечте собі комфортні умови та зосередьтеся.\nВідведіть достатньо часу для проходження тесту, оскільки ваші відповіді будуть впливати на результат.\nПам'ятайте, що це лише один з багатьох інструментів, які можуть допомогти вам у виборі професії, і рекомендації, які ви отримаєте, слід розглядати в комплексі з вашими інтересами та особистими обставинами.\nЯкщо ви готові, давайте почнемо тест на професійну орієнтацію.\nНадіємося, що цей тест допоможе вам краще зрозуміти себе та знайти шлях до задоволення в професійній діяльності!", size=20, color="grey900", italic=True, height=430, width=1200, )
                                                        ],
                                                         alignment=ft.MainAxisAlignment.CENTER,
                                                    ),
                                                  
                                                    ft.Row(
                                                        [
                                                            ft.OutlinedButton(
                                                                content=ft.Container(
                                                                    content=ft.Column(
                                                                        [
                                                                          ft.Text(value="Розпочати тест", size=20),
                                                                        ],
                                                                         alignment=ft.MainAxisAlignment.CENTER,   
                                                                    ),
                                                                ),
                                                                width=500, 
                                                                height=60, 
                                                                style=ft.ButtonStyle(ft.colors.INDIGO_900, bgcolor='indigo50',                 
                                                                side=ft.BorderSide(1,ft.colors.BLACK)),
                                                                on_click=lambda _: page.go("/test")
                                                            ),

                                                        ],
                                                         alignment=ft.MainAxisAlignment.CENTER,
                                                    ),  
                                                ]
                                            ),
                                        ),    
                                    )                   
                                ),    
                            ]
                        ),
                    ]
                )
            )

        if  page.route == "/test":
            page.views.append(
                ft.View(
                      "/test",
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

                                ft.Row(
                                    [
                                        ft.IconButton(icon=ft.icons.OUTPUT_OUTLINED, width=80, style=ft.ButtonStyle(color={
                                        ft.MaterialState.HOVERED: ft.colors.WHITE,
                                        ft.MaterialState.DEFAULT: ft.colors.INDIGO_500,
                                        }), icon_size=40, tooltip= "Вихід",  on_click=lambda _: page.go("/"))
                                    ],
                                        alignment=ft.MainAxisAlignment.END
                                ),

                                ft.Container(
                                    margin=ft.margin.only(top=175),
                                    alignment=ft.alignment.center,
                                    content=ft.Card(
                                        content=ft.Container(
                                            height=350,
                                            width=400,
                                            padding=30,
                                            content=ft.Column(
                                                [
                                                    
                                                ],))))])]))

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page_resize(None)


ft.app(target=main)
