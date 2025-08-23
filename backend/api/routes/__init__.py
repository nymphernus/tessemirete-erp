from .customers import router as customers_router
from .products import router as products_router
from .orders import router as orders_router
from .dashboard import router as dashboard_router

__all__ = ["customers_router", "products_router", "orders_router", "dashboard_router"]