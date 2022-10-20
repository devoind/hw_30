from django.urls import path
from ads.views import AdListView, AdDetailView, AdCreateView, AdDeleteView, AdUpdateView

urlpatterns = [
    path('', AdListView.as_view(), name='all_ad'),
    path('<int:pk>/', AdDetailView.as_view(), name='detail_ad'),
    path('create/', AdCreateView.as_view()),
    path('<int:pk>/upload_image/', AdUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
]
