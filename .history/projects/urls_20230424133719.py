from django.urls import path
from receipts.views import (
    show_receipts,
    create_receipt,
    category_list,
    account_list,
    create_category,
    create_account,
)

urlpatterns = [
    path("", show_receipts, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("categories/create/", create_category, name="create_create"),
    path("accounts/", account_list, name="account_list"),
    path("accounts/create/", create_account, name="create_account"),
]
