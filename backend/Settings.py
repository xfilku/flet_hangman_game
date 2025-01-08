"""
settings.py

This module provides functions for handling file reading, processing the maximum number of allowed mistakes, 
and managing file selection events for the application.

Functions:
    read_file(page, path, router):
        Reads a file and processes the words contained in it.
        
    handle_file_select(event, page, router):
        Handles the file selection event and reads the selected file.
        
    on_max_mistakes_input_clicked(page, router, value):
        Handles the setting of the maximum number of mistakes allowed in the game.

Usage:
    Import this module to handle file reading, setting maximum mistakes, and processing file selection in the app.
"""

import flet as ft
from backend.Snack import add_snack
from backend.CurrentRoute import CurrentRoute

def read_file(page, path, router):
    """
    Reads the content of a file and processes it as a list of words.

    Args:
        page (ft.Page): The page instance where snack bars and session data are updated.
        path (str): The file path to read from.
        router (Router): The router instance to reload the page after processing the file.

    Returns:
        None
    """
    try:
        # Otwieramy plik w trybie odczytu
        with open(path, 'r') as file:
            file_content = file.read()
            elements = file_content.split(',')  # Dzielimy zawartość pliku po przecinkach
            elements = [element.strip() for element in elements]  # Usuwamy zbędne spacje
            # Wyświetlamy komunikat o sukcesie
            add_snack(color=ft.Colors.GREEN, content=f"Pomyślnie dodano {len(elements)} słówek", page=page)
    except Exception as e:
        # Jeśli wystąpi błąd, wyświetlamy komunikat o błędzie
        add_snack(content="Błąd przy wczytywaniu pliku", color=ft.Colors.RED)
        return

    # Ustawiamy w sesji słówka
    page.session.set("words", elements)

def handle_file_select(event, page, router):
    """
    Handles the file selection event and processes the selected file.

    Args:
        event (FilePickerResult): The event containing the file selection data.
        page (ft.Page): The page instance to interact with the user interface.
        router (Router): The router instance to reload the page after file processing.

    Returns:
        None
    """
    # Obsługujemy wybór pliku
    if event.files:  # Sprawdzamy, czy plik został wybrany
        selected_file = event.files[0]  # Wybieramy pierwszy plik
        read_file(page=page, path=selected_file.path, router=router)  # Wywołujemy funkcję do wczytania pliku
        # Tworzymy obiekt CurrentRoute
        cr = CurrentRoute(page=page)
        # Ponownie ładujemy stronę
        router.reload_page(current_route=cr, page=page)

def on_max_mistakes_input_clicked(page, router, value):
    """
    Handles the input for setting the maximum number of mistakes allowed.

    Args:
        page (ft.Page): The page instance where the session data is updated.
        router (Router): The router instance to reload the page after setting the value.
        value (str): The input value for the maximum number of mistakes.

    Returns:
        None
    """
    try:
        # Próbujemy zapisać wartość maksymalnej liczby błędów do sesji
        page.session.set("max_mistakes", int(value))
        # Wyświetlamy komunikat o sukcesie
        add_snack(content="Zapisano ustawienie", color="green", page=page)
    except Exception as e:
        # W przypadku błędu wyświetlamy komunikat z kodem błędu
        add_snack(content=f"Zapisanie ustawienia nie powiodło się. Kod błędu: {e}", color="red", page=page)
    finally:
        # Tworzymy obiekt CurrentRoute
        cr = CurrentRoute(page=page)
        # Ponownie ładujemy stronę
        router.reload_page(current_route=cr, page=page)
