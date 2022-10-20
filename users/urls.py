from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import UserCreateView, UserListView, UserDeleteView, UserUpdateView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='all_users'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail_users'),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
]
