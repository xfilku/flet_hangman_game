"""
main.py

This is the entry point of the Flet application. It sets up the application routing, 
navigation bar, and initializes the starting page.

Functions:
    main(page: ft.Page): Sets up the application, including routing and navigation bar, 
                         and initializes the starting page.

Usage:
    Run this file to start the Flet application.
"""

import flet as ft
from routes import router
from user_controls.appbar import NavBar

def main(page: ft.Page):
    """
    Initializes the main application.

    Args:
        page (ft.Page): The main page object provided by the Flet framework.

    This function:
        1. Sets up the navigation bar based on the current route.
        2. Configures route changes and updates the page accordingly.
        3. Sets the starting page and routing logic.
    """
    # Ustawienie początkowego appbara w zależności od trasy
    page.appbar = NavBar(page)  # Musimy przekazać page do NavBar

    # Obsługa zmian tras i przekazywanie page do aktualizacji appbara
    # Przekazujemy route do routera, aby mógł zarządzać zmianami
    page.on_route_change = lambda route: router.route_change(route, page)  

    # Przypisanie routera do page (pozwala na dostęp w AppBarze)
    page.router = router  # Dodajemy router do page, co pozwala na globalny dostęp

    # Rozpoczęcie od odpowiedniej trasy
    # Dodajemy dynamiczną treść aplikacji, która jest zarządzana przez router
    page.add(router.body)
    
    # Przechodzimy do strony głównej po uruchomieniu aplikacji
    page.go('/')  
    page.update()  # Aktualizujemy stronę, aby odzwierciedlić zmiany

# Uruchomienie aplikacji
# Funkcja ft.app uruchamia główną pętlę aplikacji z targetem main
ft.app(target=main)
