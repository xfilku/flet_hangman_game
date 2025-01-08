"""
settings_view.py

This module defines the SettingView, which is the settings page of the Hangman game. 
It provides functionality to upload a file containing words and set the maximum 
number of allowed mistakes in the game.

Functions:
    SettingView(router, page):
        Renders the settings page where the user can upload a file with words and
        set the maximum number of allowed mistakes for the game.
"""

import flet as ft
from backend.Settings import handle_file_select, on_max_mistakes_input_clicked

def SettingView(router, page):
    """
    Renders the settings page where the user can upload a file with words and set 
    the maximum number of allowed mistakes.

    Args:
        router (Router): The router instance used for navigating between pages.
        page (ft.Page): The Flet page instance where the UI components will be added.

    Returns:
        ft.Column: The Flet column containing the settings page UI.
    """

    # Tworzymy kontrolkę do wyboru pliku
    file_picker = ft.FilePicker(
        on_result=lambda e: handle_file_select(e, page, router)  # Wywołanie funkcji z Settings
    )

    # Przyciski
    open_file_picker_btn = ft.ElevatedButton(
        text="Wybierz plik",
        on_click=lambda e: file_picker.pick_files()  # Otwiera FilePicker
    )

    # Pobranie wartości liczby maksymalnych pomyłek z sesji
    max_mistakes = page.session.get("max_mistakes") 
    max_mistakes_input = ft.TextField(
        hint_text="Podaj liczbę akceptowalnych pomyłek",
        value=max_mistakes,
        on_submit=lambda e: on_max_mistakes_input_clicked(page, router, max_mistakes_input.value),  # Wywołanie funkcji z Settings
        width=300
    )

    # Tekst informacyjny
    hint_text = ft.Text("Liczba dopuszczalnych pomyłek:")

    # Kolumna, która będzie zawierać przycisk
    content = ft.Column(
        controls=[
            hint_text,
            max_mistakes_input,
            open_file_picker_btn,
        ]
    )

    # Sprawdzamy, czy słowa zostały dodane do sesji
    if not page.session.contains_key("words") or len(page.session.get("words")) == 0:
        content.controls.append(ft.Text("Nie dodano żadnych słówek!", color=ft.Colors.RED))
    else:
        content.controls.append(ft.Text(f"Dodano pulę {len(page.session.get('words'))} słówek", color=ft.Colors.GREEN))
    
    # Dodajemy FilePicker i content na stronę
    page.add(
        file_picker,  # Dodajemy kontrolkę FilePicker
        content
    )

    return content  # Zwrócenie zawartości
