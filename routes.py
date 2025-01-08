from Router import Router, DataStrategyEnum
# nonlogged
from views.index_view import IndexView
from views.info_view import InfoView

router = Router(DataStrategyEnum.QUERY)

# Rejestracja tras
router.routes = {
  "/": IndexView,  # Strona główna
  "/info" : InfoView,
}
