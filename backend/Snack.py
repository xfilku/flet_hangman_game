"""
snack.py

This module provides a utility function to display snack bars (temporary notifications) on the page.

Functions:
    add_snack(page=None, color=ft.Colors.INDIGO_ACCENT_100, content=None, duration=1500, font_color=ft.Colors.BLACK):
        Displays a snack bar on the page with the specified properties.

Usage:
    Import this module and call the `add_snack` function to show a snack bar notification on the page.
"""

import flet as ft

def add_snack(page=None, color=ft.Colors.INDIGO_ACCENT_100, content=None, duration=1500, font_color=ft.Colors.BLACK):
    """
    Displays a snack bar notification on the given page.

    Args:
        page (ft.Page, optional): The page instance where the snack bar will be displayed.
                                  Must be provided, otherwise an exception is raised.
        color (str, optional): The background color of the snack bar. Default is INDIGO_ACCENT_100.
        content (str, optional): The text content of the snack bar. Default is None.
        duration (int, optional): The duration (in milliseconds) for which the snack bar will be visible. Default is 1500.
        font_color (str, optional): The color of the text inside the snack bar. Default is BLACK.

    Raises:
        Exception: If the `page` argument is not provided.

    Returns:
        None
    """
    if page is None:
        raise Exception("Nie przekazano page")  # Wyjątek, gdy nie przekazano obiektu `page`

    # Tworzenie snack bara z podanymi ustawieniami
    snack_bar = ft.SnackBar(
        content=ft.Text(content, color=font_color),  # Treść i kolor czcionki snack bara
        bgcolor=color,  # Kolor tła snack bara
        duration=duration,  # Czas trwania snack bara w milisekundach
        open=True,  # Ustawienie snack bara jako otwartego
    )
    
    # Dodanie snack bara do nakładki strony
    page.overlay.append(snack_bar)
    page.update()  # Aktualizacja widoku strony
