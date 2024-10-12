from django.urls import path
from .views import CustomModelListView, CustomModelDetailView

urlpatterns = [
    path('', CustomModelListView.as_view(), name='model_list'),
    path('<int:pk>/', CustomModelDetailView.as_view(), name='model_detail'),
]
