from django.views.generic import DetailView

from bookapp.models import Book
from bookshelfapp.models import Bookshelf


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'target_book'
    template_name = 'bookapp/bookdetail.html'

    def get_context_data(self, **kwargs):
        book = self.object
        user = self.request.user
        if user.is_authenticated:
            bookshelf = Bookshelf.objects.filter(user=user, book=book)
        context = super().get_context_data(**kwargs)
        return super(BookDetailView, self).get_context_data(context=context, bookshelf=bookshelf,**kwargs)