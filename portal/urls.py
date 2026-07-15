from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import job_detail, handle_applicant, user_register_view, user_login_view, dashboard_view, root_redirect_view

urlpatterns = [
    path("", root_redirect_view, name="root"),
    path("job/<int:pk>/", job_detail, name="job-detail"),
    path("job/<int:pk>/handle", handle_applicant, name="handle-applicant"),
    path("register/", user_register_view, name="user-register"),
    path("login/", user_login_view, name="user-login"),
    path("logout/", LogoutView.as_view(next_page="user-login"), name="logout"),
    path("dashboard/", dashboard_view, name="dashboard")
]