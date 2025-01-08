"""
index_view.py

This module defines the IndexView, which represents the home page of the application. 
The page includes buttons for navigating to the game view and the settings view.

Functions:
    IndexView(router, page):
        Renders the home page of the application with buttons to navigate to the game 
        view and settings view.
"""

import flet as ft

def IndexView(router, page):
    """
    Renders the home page of the application.

    This page contains two buttons:
        - Play: Navigates to the game page ("/play").
        - Settings: Navigates to the settings page ("/settings").

    Args:
        router (Router): The router instance used for navigating between pages.
        page (ft.Page): The Flet page instance where the UI components will be added.

    Returns:
        ft.Row: The Flet layout containing the home page UI.
    """
    
    # Jeśli nie ma ustawionej liczby dopuszczalnych pomyłek w sesji, ustawiamy ją na domyślną wartość 7
    if not page.session.contains_key("max_mistakes"):
        page.session.set("max_mistakes", 7)

    # Ustawienie strony i routera w sesji
    page.session.set("page", page)
    page.session.set("router", router)

    # Funkcja obsługująca kliknięcie przycisku "Graj"
    def play_btn_clicked(e):
        page.go('/play')  # Przechodzi do strony gry
    
    # Funkcja obsługująca kliknięcie przycisku "Ustawienia"
    def settings_btn_clicked(e):
        page.go('/settings')  # Przechodzi do strony ustawień
    
    # Przyciski
    play_btn = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.PLAY_ARROW, size=40),
                ft.Text("Graj", size=40)
            ],
            height=70,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        on_click=play_btn_clicked  # Obsługuje kliknięcie przycisku "Graj"
    )

    settings_btn = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.SETTINGS, size=40),
                ft.Text("Ustawienia", size=40)
            ],
            height=70,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        on_click=settings_btn_clicked  # Obsługuje kliknięcie przycisku "Ustawienia"
    )

    # Tytuł aplikacji
    title = ft.Text(
        "Wisielec",  # Tytuł gry
        width=300,
        size=50,
        weight=ft.FontWeight.W_700,
        color=ft.Colors.INDIGO_ACCENT_100,
        text_align=ft.TextAlign.CENTER
    )

    # Kolumna z przyciskami
    menu_column = ft.Column(
        width=300,
        spacing=20,
        controls=[
            title,  # Tytuł
            play_btn,  # Przycisk "Graj"
            settings_btn,  # Przycisk "Ustawienia"
        ],
    )
    
    # Zwrócenie układu w postaci wiersza (row) z menu
    return ft.Row(
        width=page.width,
        controls=[
            ft.Column(
                controls=[
                    menu_column  # Kolumna z przyciskami
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER  # Wyśrodkowanie elementów
    )
