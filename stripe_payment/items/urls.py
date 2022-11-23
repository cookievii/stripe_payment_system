from django.urls import path
from items.views import (CancelView, SuccessView, buy_item, item_detail,
                         item_list)

app_name = "items"

urlpatterns = [
    path("", item_list, name="item_list"),
    path("item/<int:pk>/", item_detail, name="item_detail"),
    path("buy/<int:pk>/", buy_item, name="buy_item"),
    path("cancel/", CancelView.as_view(), name="cancel"),
    path("success/", SuccessView.as_view(), name="success"),
]
