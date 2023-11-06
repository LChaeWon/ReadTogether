from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, RedirectView
from django.urls import reverse

from bookapp.models import Book
from bookshelfapp.models import Bookshelf


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
    
