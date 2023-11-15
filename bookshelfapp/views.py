import self as self
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, RedirectView, ListView, CreateView
from django.urls import reverse
from django.views.generic.edit import FormMixin

from bookapp.models import Book
from bookshelfapp.models import Bookshelf
from reviewapp.forms import WriteForm


class BookShelfView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse('bookapp:detail', kwargs={'pk': self.request.GET.get('book_pk')})
    
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.request.GET.get('book_pk'))
        user = self.request.user
        bookshelf = Bookshelf.objects.filter(user=user,book=book)
        if bookshelf.exists():
            bookshelf.delete()
        else:
            Bookshelf(user=user, book=book).save()
        return super(BookShelfView, self).get(request, *args, **kwargs)
    

class BookshelfListView(ListView):
    model = Book
    context_object_name = 'mybook_list'
    template_name = 'bookshelfapp/list.html'

    def get_queryset(self):
        mybook_list = Bookshelf.objects.filter(user=self.request.user)
        return mybook_list



class ReviewDetailView(DetailView, FormMixin):
    model = Book
    form_class = WriteForm
    context_object_name = 'target_book'
    template_name = 'bookshelfapp/review.html'
