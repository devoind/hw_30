from django.urls import path

from users.views import UserCreateView, UserListView, UserDeleteView, UserUpdateView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
]
