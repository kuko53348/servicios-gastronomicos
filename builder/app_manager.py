import flet as ft

from controls.app_screen_db import GLOBAL_VAR
from builder import builder_screens
from controls.views.nav_bar.nav_app_bar import nav_app_bar, nav_drawer_widget
from controls.views.nav_bar.nav_bar_footer import botton_bar

from builder.builder_screens import screen_view


class got_to_screen():
    """
    EVENT CHANGE SCREENS
    """

    def __init__(self,
                 to_screen='screen_name',
                 style='ring',
                 time_style=0.8,
                 page="",
                 rotation: bool = False,
                 ):
        super().__init__()

        # GET ROTATION MODULE ACCEPT
        self.rotation = rotation
        self.page = page

        # GET BY DEFOULD MAIN SCREEN FIRST
        self.widget_screen = GLOBAL_VAR(get_global_var=to_screen)

        self.page.views[0].controls.clear()
        self.page.views[0].controls.append(self.widget_screen(main_page=self.page))

        self.page.views[0].appbar.visible = True
        self.page.views[0].navigation_bar.visible = True

        # GO DEFAULD ROOT PAGE
        self.page.go('/')
