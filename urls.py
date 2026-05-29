from django.urls import path
from .views import add_product, success

urlpatterns = [
path("add-product/", add_product, name="add_product"),
path("success/", success, name="success"),
]
