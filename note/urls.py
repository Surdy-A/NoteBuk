from django.urls import path
from .views import (NoteListView, NoteDetailView, NoteDeleteView,
                    NoteCreateView, NoteUpdateView, CategoryListView,
                    SearchResultsListView, show_note_category, category_list)

app_name = 'note'

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    path('new/', NoteCreateView.as_view(), name='note_new'),
    path('category/<slug:category_slug>',
         show_note_category,
         name='show_note_by_category'),
    path('search-result',
         SearchResultsListView.as_view(),
         name='search_results')
]