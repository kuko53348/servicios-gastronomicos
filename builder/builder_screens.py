import flet as ft
from controls.app_screen_db import GLOBAL_VAR


class screen_view(ft.Container):
    """
    SCREEN_VIEW:

    MODEL BASIC OF EACH PAGE IN PAGE.CONTROL.
    I MADE WORK WITH CONTROLS BECOUSE PAGE.VIEW STILL HAVE TO MAKE SOME
    INTERNAL CHAGES TO SHOW NAV_DRAWER CORRECTLY, ONLY PERPOUSE
    OF THIS CODE IS BUILD ONE CONTAINER BOX WITH ALL ANIMATION PRELOADED
    AND MAY WORK WITH ANIMATION BETWEN SCREENS

    """

    def __init__(self,
                 page,
                 visible: bool = True,
                 alignment: object = ft.alignment.center,
                 bgcolor: str = "Transparent",
                 session_id: str = "",
                 width: int = 0,
                 height: int = 0,
                 padding: tuple = (0, 0, 0, 0),
                 pos_hint: tuple = (0, 0),
                 content: object = object(),
                 ):
        super().__init__()
        # MAIN PAGE
        self.page = page

        # SESSION ID
        self.session_id = session_id

        # ATTRIBUTES CONTAINER
        self.visible = visible
        self.height = self.page.height
        self.width = self.page.width
        self.tmp_padding = padding
        self.tmp_offset = pos_hint

        self.expand = True
        self.ink = False
        self.bgcolor = bgcolor

        # ANIMATION

        # OPCITY
        self.animate_opacity = 200

        # ROTATE
        self.rotate = ft.transform.Rotate(0, alignment=ft.alignment.center)
        self.animate_rotation = ft.animation.Animation(
            300, )

        # SCALE
        self.scale = ft.transform.Scale(scale=1)
        self.animate_scale = ft.animation.Animation(
            150, )

        # ANIMATE
        self.offset = ft.transform.Offset(0, 0)
        self.animate_offset = ft.animation.Animation(100,)

        # BOUNCE
        self.animate = ft.animation.Animation(
            1000, ft.AnimationCurve.BOUNCE_OUT)

        # self.shadow = ft.BoxShadow(
        #     spread_radius=1,
        #     blur_radius=15,
        #     color=ft.colors.BLACK,
        #     offset=ft.Offset(0, 0),
        #     blur_style=ft.ShadowBlurStyle.OUTER,
        # )

        self.content_widget = content
        # self.on_hover=lambda _:self.session_id_now(main_id=self.session_id)

    def build(self):
        self.content = self.content_widget

    def session_id_now(self, main_id):
        print(f"[]>>> ID : {main_id}")
        GLOBAL_VAR(set_global_var={main_id: self.content})
        GLOBAL_VAR(set_global_var={'current_session': main_id})
