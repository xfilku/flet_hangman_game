import flet as ft

def NavBar(page):
    NavBar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda _: page.router.go_back(page),
            ),
            leading_width=40,
            title=ft.Text(f"Wisielec"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.Icons.QUESTION_ANSWER, on_click=lambda _: page.go('/info')),
            ]
        )
    return NavBar
