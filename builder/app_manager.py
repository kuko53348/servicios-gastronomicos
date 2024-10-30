import flet as ft

from controls.app_screen_db import GLOBAL_VAR
from controls.views.nav_bar.nav_app_bar import nav_app_bar, nav_drawer_widget
from controls.views.nav_bar.nav_bar_footer import botton_bar


class got_to_screen():
    """
    EVENT CHANGE SCREENS
    """
    def __init__(self,
                 page: object = object(),
                 rotation: bool = False,
                 style: str = 'ring',
                 time_style: float = 0.8,
                 to_screen: str = 'screen_name',
                 ):
        # super().__init__()

        # GET ROTATION MODULE ACCEPT
        self.page = page
        self.rotation = rotation

        # GET BY DEFOULD MAIN SCREEN FIRST
        self.widget_screen = GLOBAL_VAR(get_global_var=to_screen)

        # VIEWS IN MAIN PAGE
        self.main_view = self.page.views[0]

        # CLEAR CONTROL VIEW TO ADD CURRENT SELECTED VIEW
        self.main_view.controls.clear()
        self.main_view.controls.append(self.widget_screen(main_page=self.page))

        # SET VISIBLE APPBAR AND NAVIGATION BAR
        self.main_view.appbar.visible = True
        self.main_view.navigation_bar.visible = True

        # GO BY DEFAULD ROOT PAGE
        self.page.go('/')
