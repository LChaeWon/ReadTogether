from django.shortcuts import render
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
        # object_list = Book.objects.filter(book=self.get_object())
        # return super(BookDetailView,self).get_context_data(object_list=object_list, bookshelf=bookshelf,**kwargs)
        context = super().get_context_data(**kwargs)
        return super(BookDetailView, self).get_context_data(context=context, bookshelf=bookshelf,**kwargs)

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books = Book.objects.filter(title__contains=searched)
        return render(request, 'bookapp/searched.html', {'searched': searched, 'books': books})
    else:
        return render(request, 'bookapp/searched.html', {})