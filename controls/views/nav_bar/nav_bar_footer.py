import time
import flet as ft
from builder import app_manager
from builder.app_manager import GLOBAL_VAR


class botton_bar(ft.BottomAppBar):

    def __init__(self, visible: bool = False, main_page: object = object()):
        super().__init__()
        self.bgcolor = ft.colors.TRANSPARENT
        self.main_page = main_page
        self.offset = (0, 0)
        self.visible = visible

    def build(self):
        self.content = ft.Container(
            ink=False,
            bgcolor="White,0.03",
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(32),
            padding=0,
            margin=0,
            border=ft.border.all(4, "WHITE,0.04"),
            blur=(18, 18),
            content=ft.CupertinoSlidingSegmentedButton(
                selected_index=2,
                thumb_color="WHITE,0.06",
                bgcolor="TRANSPARENT",
                padding=ft.padding.symmetric(0, 10),

                controls=[
                    ft.Container(
                        width=89,
                        content=ft.Icon(
                            name="arrow_back_ios_outlined"),
                    ),
                    ft.Container(
                        width=89,
                        content=ft.Icon(name="HOME"),
                    ),
                    ft.Container(
                        width=89,
                        content=ft.Icon(
                            name="widgets_rounded"),

                    ),
                ],
                on_change=lambda e: self.event_bottom_appbar(
                    data=e.data),
            ),  # <=== NOTE COMA
        )

    def event_bottom_appbar(self, data):  # ID: main_screen, event_Iconbutton
        # RESET DEFOUD FALSE SECOND SCREEN
        GLOBAL_VAR(set_global_var={
            'secundary_menu_show': False,
        })

        list_screen: dict = {

            "0": "second_screen",
            "1": "first_screen",
            "2": "doc_screen",

        }
        current_screen = GLOBAL_VAR(get_global_var='current_screen')

        if data == "0":
            if not current_screen == "Please no exist input in database":
                app_manager.got_to_screen(
                    to_screen='second_screen',
                    style='burble',
                    time_style=0.8,
                    page=self.main_page,
                )

        if data == "1":
            app_manager.got_to_screen(
                # rotation=True,
                to_screen='first_screen',
                style='burble',
                time_style=0.8,
                page=self.main_page,
            )

        time.sleep(0.3)

        GLOBAL_VAR(set_global_var={'show_off': True})
        self.content.content.selected_index = 2
        self.content.update()
