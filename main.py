import flet as ft
from routes import router
from user_controls.appbar import NavBar

def main(page: ft.Page):
    # Ustawienie początkowego appbara w zależności od trasy
    page.appbar = NavBar(page)  # Musimy przekazać page do NavBar

    # Obsługa zmian tras i przekazywanie page do aktualizacji appbara
    page.on_route_change = lambda route: router.route_change(route, page)  # Przekazujemy tylko route

    # Przypisanie routera do page (pozwala na dostęp w AppBarze)
    page.router = router  # Dodajemy router do page

    # Rozpoczęcie od odpowiedniej trasy
    page.add(router.body)
    page.go('/')  # Rozpoczynamy od strony głównej
    page.update()

# Uruchomienie aplikacji
ft.app(target=main, assets_dir="assets")
