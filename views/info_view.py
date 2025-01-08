"""
info_view.py

This module defines the InfoView, which represents the information page of the 
application. The page displays the rules and description of the Hangman game, 
as well as a button to start the game.

Functions:
    InfoView(router, page):
        Renders the information page with the game description and rules.
"""

import flet as ft

def InfoView(router, page):
    """
    Renders the information page with the game description and rules.

    The page displays an overview of how to play the Hangman game, including the
    rules and how to start the game. A button is also provided to navigate 
    to the main page and start playing.

    Args:
        router (Router): The router instance used for navigating between pages.
        page (ft.Page): The Flet page instance where the UI components will be added.

    Returns:
        ft.ListView: The Flet ListView containing the information page UI.
    """
    
    # Opis gry w wisielca
    game_info_text = """
    Gra w wisielca to klasyczna zabawa słowna, w której gracz stara się odgadnąć
    ukryte słowo, zgadując litery. Zaczynasz od wyświetlenia pustych podkreśleń,
    które reprezentują litery słowa do odgadnięcia. Twoim zadaniem jest odgadnąć
    słowo, proponując litery, zanim popełnisz zbyt wiele błędów.

    Jak zagrać?
    1. Przejź do ustawień i określ swoje własne słowa
    2. Mozesz tam też ustalić ilość dopuszczalnych błędów
    3. Kliknij Graj!

    Zasady:
    1. Wybierasz literę, którą chcesz zgadnąć.
    2. Jeśli litera znajduje się w słowie, zostaje ujawniona w odpowiednich miejscach.
    3. Jeśli litera nie znajduje się w słowie, liczba błędów wzrasta.
    4. Gra kończy się, gdy zgadniesz całe słowo lub przekroczysz maksymalną liczbę błędów.

    Cel:
    Celem gry jest odgadnięcie całego słowa, zanim liczba błędów osiągnie maksymalną dozwoloną liczbę.

    W ustawieniach możesz:
    - Wczytać słowa, z których będą losowane wyrazy do gry.
    - Określić maksymalną liczbę błędów, które można popełnić w trakcie gry.

    Aby rozpocząć grę, kliknij przycisk "Graj".
    """
    
    # Zawartość strony info, opakowana w ListView dla przewijania
    content = ft.ListView(
        [
            ft.Text("Zasady gry w Wisielca", size=24, text_align=ft.TextAlign.CENTER),  # Tytuł
            ft.Text(game_info_text, size=18, text_align=ft.TextAlign.LEFT),  # Opis gry
            ft.ElevatedButton(
                text="Graj", on_click=lambda e: page.go("/"), width=300, height=70  # Przechodzenie do gry
            ),
        ],
        expand=True,  # Zawartość rozciąga się na dostępne miejsce
        spacing=10,   # Odstępy między elementami
        padding=10,   # Odstępy wewnętrzne
    )
    
    page.add(content)  # Dodanie zawartości do strony
    return content  # Zwrócenie zawartości
