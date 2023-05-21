from posixpath import expanduser
from turtle import color
import flet as ft
from flet_core.icons import EXPAND


class Home(ft.UserControl):
    def build(self):
        return ft.Row(
            [
                ft.Container(
                    image_src=(f"https://github.com/VasinIgor96/New-Project/blob/master/Fonnn.jpg?raw=true"),
                    height=720,
                    width=1080,
                    content=ft.Card(
                        content=ft.Container(
                            
                            height=400,
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
                                        [ft.Checkbox(label="Я погоджуюсь з умовами обробки\n перснальних данних", value=False, fill_color=ft.colors.BLUE_900)],
                                        
                                    ),

                                    ft.Row( 
                                        [ft.ElevatedButton("Далі", width=120, style=ft.ButtonStyle (ft.colors.BLUE_900, side=ft.BorderSide(2, ft.colors.BLUE_900)))],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            ),
                            width=400,
                            padding=25,
                        )
                    ),
                    expand=True,
                    alignment=ft.alignment.center
                )
            ],
            alignment=ft.alignment.center
        )
        