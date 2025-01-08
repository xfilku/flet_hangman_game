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
        leading=ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda _: page.router.go_back(page),  # Funkcja obsługująca powrót do poprzedniej trasy
        ),
        leading_width=40,  # Szerokość ikony wiodącej (np. strzałki)
        title=ft.Text(f"Wisielec"),  # Tytuł aplikacji wyświetlany na AppBarze
        center_title=False,  # Tytuł nie jest wyśrodkowany
        bgcolor=ft.Colors.INDIGO_ACCENT_100,  # Kolor tła AppBara
        actions=[
            ft.IconButton(ft.Icons.QUESTION_MARK_OUTLINED, on_click=lambda _: page.go('/info')),  # Ikona prowadząca do strony informacji
        ]
    )
    return NavBar
