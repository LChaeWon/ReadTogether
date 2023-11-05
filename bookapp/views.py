from django.views.generic import DetailView

from bookapp.models import Book


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'target_book'
    template_name = 'bookapp/bookdetail.html'