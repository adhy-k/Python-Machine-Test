from django.urls import path
from . import views

urlpatterns = [
    # UI pages
    path("", views.ui_home, name="home"),
    path("ui/register/", views.ui_register, name="ui_register"),
    path("ui/users/", views.ui_users, name="ui_users"),
    path("ui/expenses/summary/", views.ui_expenses_summary, name="ui_expenses_summary"),

    path("register/", views.register, name="register"),
    path("users/", views.get_users, name="users_list"),
    path("users/<int:user_id>/", views.user_detail, name="user_detail"),
    path("expenses/summary/", views.expenses_summary, name="expenses_summary"),
]
