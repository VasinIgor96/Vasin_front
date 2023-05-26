from posixpath import expanduser
from turtle import color
import flet as ft
from flet_core.icons import EXPAND


class Home(ft.UserControl):
    def build(self):
        return ft.Stack(
            [
                ft.Row(
                    [
                    ft.Image(
                        f"https://github.com/VasinIgor96/New-Project/blob/master/Fonnn.jpg?raw=true", 
                        fit=ft.ImageFit.CONTAIN,
                        #width = 2000,
                        #height=2000,
                        
                        ),
                        ]
                   
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
                                        [ft.Checkbox(label="Я погоджуюсь з умовами обробки\n перснальних данних", value=False, fill_color=ft.colors.BLUE_900)],
                                        
                                    ),

                                    ft.Row(
                                        [ft.ElevatedButton("Далі", width=120, style=ft.ButtonStyle (ft.colors.BLUE_900, side=ft.BorderSide(2, ft.colors.BLUE_900)), on_click=go_store())],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            ),
                           
                        )
                    ),
                   ),
             
            ],
             
        )
