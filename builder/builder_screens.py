import flet as ft

class screen_view(ft.Container):
    """
    :SCREEN_VIEW:

    WRAPED BOX CONTAINER THAT CONTENT EACH SELECTED SCREEN
    HAVE INSIDE EFFECTS BY DEFOULD

    :ATTRIBUTES:

    animate
    animate_offset
    animate_opacity
    animate_rotation
    animate_scale
    offset
    rotate
    scale
    """

    def __init__(self,
                 page: object = object(),
                 alignment: object = ft.alignment.center,
                 bgcolor: str = "Transparent",
                 content: object = object(),
                 height: int = 0,
                 padding: tuple = (0, 0, 0, 0),
                 pos_hint: tuple = (0, 0),
                 session_id: str = "",
                 visible: bool = True,
                 width: int = 0,
                 ):
        # super().__init__()

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

    def build(self):
        self.content = self.content_widget
