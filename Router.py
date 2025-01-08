"""
Router.py

This module defines the `Router` class and `DataStrategyEnum` enumeration 
to manage routing logic and handle navigation between different views 
in a Flet application.

Classes:
    DataStrategyEnum: Enum to represent different strategies for data management.
    Router: A custom routing manager for handling navigation, URL query parsing, 
            and page rendering in the application.

Functions:
    route_change(route, page): Updates the current page content based on the route.
    go_back(page): Navigates to the previous route in history.
    reload_page(current_route, page): Reloads the current page.

Usage:
    The `Router` class is used as a central mechanism for defining and managing 
    application routes and navigation.
"""

from enum import Enum
import flet as ft

class DataStrategyEnum(Enum):
    """
    Enumeration to represent different data management strategies.

    Members:
        QUERY: Use URL query parameters for data transfer.
        ROUTER_DATA: Use router's internal data dictionary.
        CLIENT_STORAGE: Use client's local storage for persisting data.
        STATE: Use Flet's built-in state management for data transfer.
    """
    QUERY = 0
    ROUTER_DATA = 1
    CLIENT_STORAGE = 2
    STATE = 3

class Router:
    """
    A custom routing manager for handling navigation and rendering in a Flet app.

    Attributes:
        data_strategy (DataStrategyEnum): Strategy used for managing data.
        data (dict): Dictionary to store route-related data.
        routes (dict): A dictionary mapping routes to their respective handler functions.
        body (ft.Container): The main container for the app content.
        history (list): List of previously visited routes for navigation history.

    Methods:
        route_change(route, page): Updates the current page content based on the route.
        go_back(page): Navigates to the previous route in the history.
        reload_page(current_route, page): Reloads the current page with updated content.
    """

    def __init__(self, data_strategy=DataStrategyEnum.QUERY):
        """
        Initializes the Router instance.

        Args:
            data_strategy (DataStrategyEnum): The strategy used for managing data. 
                                              Defaults to DataStrategyEnum.QUERY.
        """
        self.data_strategy = data_strategy
        self.data = dict()
        self.routes = {}
        self.body = ft.Container()
        self.history = []  # Historia tras odwiedzonych w aplikacji

    def route_change(self, route, page):
        """
        Handles the logic for changing the route and updates the page content.

        Args:
            route (ft.Route): The current route object containing the route and query parameters.
            page (ft.Page): The main page object to update the displayed content.

        This method:
            1. Parses the route to extract the path and query parameters.
            2. Updates the `history` to include the new route.
            3. Renders the content based on the route's handler function.
        """
        # Parsowanie trasy oraz parametrów zapytania
        _page = route.route.split("?")[0]
        queries = route.route.split("?")[1:]

        # Dodanie trasy do historii, jeśli nie jest identyczna z poprzednią
        if not self.history or self.history[-1] != _page:
            self.history.append(_page)

        # Parsowanie parametrów zapytania i zapisanie ich w słowniku danych
        for item in queries:
            key = item.split("=")[0]
            value = item.split("=")[1]
            self.data[key] = value.replace('+', ' ')  # Zamiana '+' na spacje

        # Ustawienie zawartości strony na podstawie obsługiwanej trasy
        self.body.content = self.routes.get(_page, lambda _: ft.Text("404 Not Found"))(self, page)
        self.body.update()  # Aktualizacja kontenera
        page.update()  # Aktualizacja strony

    def go_back(self, page):
        """
        Navigates back to the previous route in the history.

        Args:
            page (ft.Page): The main page object to navigate.

        This method removes the current route from the history and 
        navigates to the previous one.
        """
        # Sprawdzenie, czy w historii są poprzednie trasy
        if len(self.history) > 1:
            self.history.pop()  # Usunięcie bieżącej trasy
            previous_route = self.history[-1]  # Pobranie poprzedniej trasy
            page.go(previous_route)  # Przejście do poprzedniej trasy

    def reload_page(self, current_route, page):
        """
        Reloads the current page with updated content.

        Args:
            current_route (ft.Route): The current route object.
            page (ft.Page): The main page object to reload.

        This method triggers a re-render of the current page content.
        """
        # Przekazanie bieżącej trasy do funkcji zmiany trasy
        self.route_change(current_route, page)
