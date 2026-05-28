from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.task_list, name='task_list'),
    path("add/", views.add_task, name='add_task'),
    path("update/<int:pk>/", views.update_task, name='update_task'),
    path("delete/<int:pk>/", views.delete_task, name='delete_task'),

    path("register/", views.register, name='register'),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name='login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),

    path("logout/", views.user_logout, name='logout'),


    # optional for login_required redirect
    path("accounts/login/", auth_views.LoginView.as_view(template_name='login.html')),
]