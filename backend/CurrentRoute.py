"""
CurrentRoute.py

This module defines the CurrentRoute class, which is used to represent the current route of the page 
in a web application. It contains details about the current route, such as the route path, data, 
and name. It also provides functionality to initialize and manage the current route.

Class:
    CurrentRoute:
        - Initializes with the current route details from the page.
"""

class CurrentRoute:
    """
    Represents the current route of the page.

    Attributes:
        route (str): The current route (URL path) of the page.
        data (str): The data associated with the current route (URL parameters).
        name (str): The name of the current route change event.

    Methods:
        __init__(page=None, route=None, name=None, data=None):
            Initializes the CurrentRoute object with the route, data, and name.

    """
    
    def __init__(self, page=None, route=None, name=None, data=None):
        """
        Initializes a CurrentRoute instance with the current route details.

        Args:
            page (ft.Page, optional): The page instance. If None, an exception is raised.
            route (str, optional): The route (URL path) for the current page. Defaults to None.
            name (str, optional): The name of the route change event. Defaults to None.
            data (str, optional): Any associated data with the route. Defaults to None.

        Raises:
            Exception: If page is None.
        """
        if page is None:
            raise Exception("Nie przekazano page")  # Exception raised if no page is passed

        self.route = page.route  # Route of the current page
        self.data = self.route  # Data associated with the route
        self.name = "route_change"  # Default name for the route change event
