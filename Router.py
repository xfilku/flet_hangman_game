from enum import Enum
import flet as ft

class DataStrategyEnum(Enum):
    QUERY = 0
    ROUTER_DATA = 1
    CLIENT_STORAGE = 2
    STATE = 3

class Router:
    def __init__(self, data_strategy=DataStrategyEnum.QUERY):
        self.data_strategy = data_strategy
        self.data = dict()
        self.routes = {}
        self.body = ft.Container()
        self.history = []  # Dodajemy historię tras

    def route_change(self, route, page):
        # DYNAMICZNE ODŚWIEŻANIE
        if page.session.get("current_rally") is not None:
            page.session.get("current_rally").update_rally(page=page)

        # Obsługa parametrów w URL
        _page = route.route.split("?")[0]
        queries = route.route.split("?")[1:]

        # Dodajemy trasę do historii, jeśli nie jest to ta sama trasa
        if not self.history or self.history[-1] != _page:
            self.history.append(_page)

        # Przetwarzanie parametrów zapytania
        for item in queries:
            key = item.split("=")[0]
            value = item.split("=")[1]
            self.data[key] = value.replace('+', ' ')

        # Ustawienie zawartości strony na podstawie trasy
        self.body.content = self.routes.get(_page, lambda _: ft.Text("404 Not Found"))(self, page)
        self.body.update()
        page.update()

    def go_back(self, page):
        """Powrót do poprzedniej trasy w historii."""
        if len(self.history) > 1:
            self.history.pop()  # Usuń bieżącą trasę
            previous_route = self.history[-1]  # Pobierz poprzednią trasę
            page.go(previous_route)  # Przejdź do poprzedniej trasy

    def reload_page(self, current_route, page):
        """Ponowne wczytanie aktualnej strony."""
        self.route_change(current_route, page)
