"""
play_view.py

This module defines the GameView, which represents the main game page of the
Hangman game. It handles the display of the word to guess, manages user input,
and tracks the game state such as the number of mistakes and the letters guessed.

Functions:
    GameView(router, page):
        Renders the game page, initializing game state, displaying the word to guess, 
        and handling user input for guessing letters.
"""

import flet as ft
from backend.Snack import add_snack
from backend.Game import *

def GameView(router, page):
    """
    Renders the main game page where the user can play the Hangman game.

    It initializes the game state, including the word to guess, the number of mistakes,
    and the letters guessed. It then displays the game interface where the user can input
    guesses and interact with the game. It also handles win/loss conditions.

    Args:
        router (Router): The router instance used for navigating between pages.
        page (ft.Page): The Flet page instance where the UI components will be added.

    Returns:
        ft.Column: The Flet column containing the game UI.
    """
    
    # Sprawdzenie, czy sesja zawiera dane dotyczące gry
    if not page.session.contains_key("words"):
        add_snack(content="Nie masz wczytanych żadnych słówek!", color=ft.Colors.RED, page=page)
        return ft.Text("Nie masz wczytanych żadnych słówek!", color=ft.Colors.RED)
    
    # Zainicjalizowanie stanu gry z sesji, jeśli dostępny
    if not page.session.contains_key("correct_word"):
        correct_word = random_word(page=page)
        page.session.set("correct_word", correct_word)
    else:
        correct_word = page.session.get("correct_word")

    # Pobranie wartości z sesji, a jeśli nie istnieje, ustawienie wartości domyślnych
    max_trials = page.session.get("max_mistakes")

    guessed_letters = page.session.get("guessed_letters")
    if guessed_letters is None:
        guessed_letters = ['_'] * len(correct_word)  # Inicjalizacja zgadywanych liter
    
    mistakes = page.session.get("mistakes")
    if mistakes is None:
        mistakes = 0  # Inicjalizacja liczby błędów
    
    guessed_letters_set = page.session.get("guessed_letters_set")
    if guessed_letters_set is None:
        guessed_letters_set = set()  # Inicjalizacja zbioru zgadniętych liter

    # Interfejs użytkownika
    word_display = ft.Text(" ".join(guessed_letters), size=50, text_align=ft.TextAlign.CENTER, width=page.width)
    used_trials = ft.Text(f"Pomyłki: {mistakes}/{max_trials}", size=20)
    word_pool = ft.Text(f"Pula słówek: {len(page.session.get('words'))}", color=ft.Colors.GREEN, size=20)
    letter_input = ft.TextField(label="Wpisz literę", autofocus=True, on_submit=lambda e: guess_letter(page, router, letter_input, correct_word, guessed_letters, mistakes, guessed_letters_set, max_trials))
    restart_btn = ft.ElevatedButton(text="Zacznij od nowa", on_click=lambda e: restart_game(page, router))

    content = ft.Column([  # Tworzenie kolumny z elementami
        word_display,
        used_trials,
        word_pool,
        letter_input
    ], alignment=ft.MainAxisAlignment.CENTER)

    if "_" not in guessed_letters:  # Gracz wygrał
        handle_win(page, content, restart_btn, word_display)
    elif mistakes >= max_trials:  # Gracz przegrał
        handle_loss(page, content, restart_btn, correct_word, word_display)

    page.add(content)  # Dodajemy zawartość na stronę po jego stworzeniu
    return content  # Zwrócenie zawartości
