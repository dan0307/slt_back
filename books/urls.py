from django.urls import path
from . import views

urlpatterns = [
    path('create-book/', views.create_book, name='create_book'),
    path('user-progress/', views.user_progress),
    path('book-progress/', views.book_progress),
    path('update-progress/', views.update_progress),
    path('check-book/<int:book_id>/<int:user_id>/', views.check_book, name='check_book'),
    path('get-progress/', views.get_progress, name='get_progress'),
    path('started-books/', views.user_started_books, name='started_books'),
]
