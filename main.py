import flet as ft

from controls.app_screen_manager import screens
from controls.app_screen_db import GLOBAL_VAR
from controls.views.nav_bar.nav_bar_footer import botton_bar
from controls.views.nav_bar.nav_app_bar import nav_app_bar, nav_drawer_widget

from builder import app_manager


def main(page: ft.Page):
    session_id = page.__dict__['_session_id']
    page.expand = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.margin = 0
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.always_on_top = True

    def route_change(route):
        """
        ALWAYS WILL BE CHANGE TO NEW USER TO ROOT '/' PAGE

        :param      route:  The route
        :type       route:  { type_description }
        """
        GLOBAL_VAR(set_global_var=screens)

        page.views.clear()
        page.views.append(
            ft.View(
                padding=0,
                route="/",
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                appbar=nav_app_bar(main_page=page),
                drawer=nav_drawer_widget(main_page=page),
                navigation_bar=botton_bar(main_page=page),
                controls=[
                    screens.get("main_screen")(main_page=page),
                ],
            )
        )
        page.update()

    page.on_route_change = route_change
    page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
    page.go('/')


def run_app():
    """
    - NO ERASE THIS FUNCTION
    - ONLY RUN CREATING PYPY PACKAGE
    """
    ft.app(
        target=main,
    )


if __name__ == '__main__':

    ft.app(
        target=main,
        assets_dir="assets",
        # view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
        # web_renderer = ft.WebRenderer.HTML,
        # port=21109,
    )
