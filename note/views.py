from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    paginate_by = 20
    template_name = 'note/note.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['order_by_created_date'] = Note.objects.order_by('-created')
        context['categories'] = Category.objects.all()
        context['author_note'] = Note.objects.filter(
            author=self.request.user).order_by('-created')
        return context


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'note/note_detail.html'
    login_url = 'login'


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ('__all__')
    template_name = 'note/note_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'note/note_delete.html'
    success_url = reverse_lazy('note:note_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'note/note_new.html'
    fields = ('__all__')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def show_note_category(request, category_slug=None):
    notes = Note.objects.all()
    category = None
    categories = Category.objects.all()

    paginator = Paginator(notes, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    shows_page = paginator.get_page(page)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        notes = notes.filter(category=category)

    return render(
        request, 'note/category.html', {
            'category': category,
            'categories': categories,
            'notes': notes,
            'shows_page': shows_page
        })


def category_list(request):
    note_categories = Category.objects.all()
    return render(request, 'base2.html', {
        'note_categories': note_categories,
    })


class CategoryListView(ListView):
    model = Category
    template_name = 'note/note.html'


class SearchResultsListView(ListView):
    model = Note
    context_object_name = 'note_search_list'
    template_name = 'note/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Note.objects.filter(
            Q(title__icontains=query) | Q(note__icontains=query))
