from .customer import *
from .product import *
from .order import *
from .dashboard import *

__all__ = ["get_customers", "create_customer", "get_customer", "update_customer", "delete_customer",
           "get_products", "create_product", "get_product", "update_product", "delete_product",
           "get_orders", "create_order", "get_order", "update_order", "delete_order",
           "get_dashboard_stats"]