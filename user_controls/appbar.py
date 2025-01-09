"""
appbar.py

This module defines the navigation bar (AppBar) used across the application.

Functions:
    NavBar(page): Creates and returns an AppBar with navigation and action buttons.

Usage:
    Import this module and use the `NavBar` function to set the AppBar for a page.
"""

import flet as ft

def NavBar(page):
    """
    Creates a navigation bar (AppBar) with a back button and an information button.

    Args:
        page (ft.Page): The current page instance, used to manage navigation.

    Returns:
        ft.AppBar: An AppBar configured with navigation and action buttons.
    """
    NavBar = ft.AppBar(
    leading=ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda _: page.router.go_back(page),  # Funkcja obsługująca powrót do poprzedniej trasy
            ),
            ft.Image(
                src="assets/logo.png",  # Ścieżka do pliku z ikoną/logo
                width=60,  # Szerokość obrazu
                height=60,  # Wysokość obrazu
                fit=ft.ImageFit.CONTAIN  # Dopasowanie obrazu
            ),
            ft.Container(width=20),  # Dodanie odstępu (20 pikseli) między logo a tytułem
        ],
        spacing=10,  # Odległość między strzałką a logo
        alignment=ft.MainAxisAlignment.START,  # Wyrównanie do lewej
    ),
    leading_width=100,  # Szerokość obszaru leading (dostosuj w zależności od szerokości logo i strzałki)
    title=ft.Text(f"Wisielec", weight=ft.FontWeight.W_500),  # Tytuł aplikacji wyświetlany na AppBarze
    center_title=False,  # Tytuł nie jest wyśrodkowany
    bgcolor=ft.Colors.INDIGO_ACCENT_100,  # Kolor tła AppBara
    actions=[
        ft.IconButton(ft.Icons.QUESTION_MARK_OUTLINED, on_click=lambda _: page.go('/info')),  # Ikona prowadząca do strony informacji
        ]
    )
    return NavBar

