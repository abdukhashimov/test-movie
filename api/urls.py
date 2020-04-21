from django.urls import path
from api.views import MovieCreateListView, MovieDetailView

urlpatterns  = [
    path('movies/', MovieCreateListView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]