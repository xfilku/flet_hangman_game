"""
game.py

This module contains functions to handle the game logic for a word-guessing game.
It includes functionality for randomly selecting a word, handling letter guesses, 
updating the display, and handling game restart, win, and loss conditions.

Functions:
    random_word(page):
        Selects a random word from the session's word pool.

    guess_letter(page, router, letter_input, correct_word, guessed_letters, mistakes, guessed_letters_set, max_trials):
        Processes the player's letter guess and updates the game state.

    update_display(page, router, guessed_letters, mistakes, max_trials):
        Updates the game interface with the current guessed letters and number of mistakes.

    restart_game(page, router):
        Resets the game session and reloads the page.

    handle_win(page, content, restart_btn, word_display):
        Handles the win condition by displaying a congratulatory message and enabling the restart button.

    handle_loss(page, content, restart_btn, correct_word, word_display):
        Handles the loss condition by displaying a loss message and showing the correct word.
"""

import random
import flet as ft
from backend.CurrentRoute import CurrentRoute
from backend.Snack import add_snack

def random_word(page):
    """
    Selects a random word from the word pool stored in the session.

    Args:
        page (ft.Page): The page instance containing the word pool in the session.

    Returns:
        str: A random word from the session's word pool.
    """
    # Wybieramy losowy indeks z dostępnych słówek
    random_index = random.randint(0, len(page.session.get("words"))-1)
    word = page.session.get("words")[random_index]
    return word

def guess_letter(page, router, letter_input, correct_word, guessed_letters, mistakes, guessed_letters_set, max_trials):
    """
    Processes the player's guess by validating the input, updating the game state, 
    and handling incorrect or repeated guesses.

    Args:
        page (ft.Page): The page instance to update the game state.
        router (Router): The router instance to reload the page.
        letter_input (ft.TextField): The input field where the player enters a letter.
        correct_word (str): The correct word to guess.
        guessed_letters (list): A list representing the guessed letters.
        mistakes (int): The number of incorrect guesses made so far.
        guessed_letters_set (set): A set containing all guessed letters.
        max_trials (int): The maximum number of allowed mistakes.

    Returns:
        None
    """
    letter = letter_input.value.strip().lower()
    letter_input.value = ""  # Resetujemy pole tekstowe

    # Sprawdzenie, czy litera jest poprawna
    if len(letter) != 1 or not letter.isalpha():
        add_snack(content="Proszę podać jedną literę!", color=ft.Colors.RED, page=page)
        cr = CurrentRoute(page=page)
        router.reload_page(current_route = cr, page=page)
        return

    # Sprawdzamy, czy litera została już zgadnięta
    if letter in guessed_letters_set:
        add_snack(content="Ta litera została już użyta!", color=ft.Colors.YELLOW, page=page)
        cr = CurrentRoute(page=page)
        router.reload_page(current_route = cr, page=page)
        return

    # Sprawdzanie, czy litera jest w słowie
    if letter in correct_word:
        for i, char in enumerate(correct_word):
            if char == letter:
                guessed_letters[i] = letter
    else:
        mistakes += 1

    # Dodajemy literę do zbioru zgadniętych liter
    guessed_letters_set.add(letter)

    # Zapisujemy stan gry w sesji
    page.session.set("guessed_letters", guessed_letters)
    page.session.set("mistakes", mistakes)
    page.session.set("guessed_letters_set", guessed_letters_set)

    # Aktualizacja widoku
    update_display(page, router, guessed_letters, mistakes, max_trials)


def update_display(page, router, guessed_letters, mistakes, max_trials):
    """
    Updates the display with the current game state, including the guessed letters 
    and the number of mistakes made.

    Args:
        page (ft.Page): The page instance to update the display.
        router (Router): The router instance to reload the page.
        guessed_letters (list): The list of guessed letters.
        mistakes (int): The number of incorrect guesses made.
        max_trials (int): The maximum number of allowed mistakes.

    Returns:
        None
    """
    # Zakładając, że to jest kontrolka dla prób
    used_trials = page.controls[1]
    # Zakładając, że to jest kontrolka wyświetlająca słowo
    word_display = page.controls[0]
    # Zakładając, że to jest kontrolka dla puli słówek
    word_pool = page.controls[2]

    used_trials.text = f"Pomyłki: {mistakes}/{max_trials}"
    word_display.text = " ".join(guessed_letters)
    word_pool.text = f"Pula słówek: {len(page.session.get('words'))}"
    
    cr = CurrentRoute(page=page)
    router.reload_page(current_route=cr, page=page)


def restart_game(page, router):
    """
    Resets the game session by removing the current game state data and reloads the page.

    Args:
        page (ft.Page): The page instance to reset the game session.
        router (Router): The router instance to reload the page.

    Returns:
        None
    """
    page.session.remove("correct_word")
    page.session.remove("guessed_letters")
    page.session.remove("mistakes")
    page.session.remove("guessed_letters_set")
    cr = CurrentRoute(page=page)  # Aktualizacja widoku
    router.reload_page(current_route=cr, page=page)

def handle_win(page, content, restart_btn, word_display):
    """
    Handles the win condition by displaying a success message, updating the word display to green, 
    disabling the letter input field, and adding a restart button.

    Args:
        page (ft.Page): The page instance to display the win message.
        content (ft.Column): The column containing the game UI elements.
        restart_btn (ft.ElevatedButton): The button to restart the game.
        word_display (ft.Text): The display showing the word being guessed.

    Returns:
        None
    """
    add_snack(content="Gratulacje, wygrałeś!", color=ft.Colors.GREEN, page=page)
    word_display.color = ft.Colors.GREEN
    content.controls[-1].disabled = True  # Disable the input field for letters after winning
    content.controls.append(restart_btn)

def handle_loss(page, content, restart_btn, correct_word, word_display):
    """
    Handles the loss condition by displaying a failure message, revealing the correct word, 
    updating the word display to red, disabling the letter input field, and adding a restart button.

    Args:
        page (ft.Page): The page instance to display the loss message.
        content (ft.Column): The column containing the game UI elements.
        restart_btn (ft.ElevatedButton): The button to restart the game.
        correct_word (str): The correct word that the player was trying to guess.
        word_display (ft.Text): The display showing the word being guessed.

    Returns:
        None
    """
    add_snack(content="Niestety, przegrałeś!", color=ft.Colors.RED, page=page)
    word_display.value = correct_word
    word_display.color = ft.Colors.RED
    content.controls[-1].disabled = True  # Disable the input field for letters after losing
    content.controls.append(restart_btn)
