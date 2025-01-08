"""
routes.py

This module sets up the application's routing by using the `Router` class from the `Router` module.
It defines the mapping between URL paths and their corresponding view functions.

Classes:
    None

Functions:
    None

Attributes:
    router (Router): An instance of the `Router` class used to manage application routes.
    routes (dict): A dictionary mapping URL paths to their corresponding view functions.

Usage:
    Import this module to access the preconfigured `router` object for routing purposes.
"""

from Router import Router, DataStrategyEnum
# Importy widoków aplikacji
from views.index_view import IndexView
from views.info_view import InfoView
from views.settings_view import SettingView
from views.play_view import GameView

# Inicjalizacja routera z wybraną strategią zarządzania danymi
router = Router(DataStrategyEnum.QUERY)

# Rejestracja tras
router.routes = {
  "/": IndexView,  # Strona główna
  "/info": InfoView,  # Strona informacji
  "/settings": SettingView,  # Strona ustawień
  "/play": GameView  # Strona gry
}
