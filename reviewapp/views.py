from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from bookapp.models import Book
from reviewapp.forms import WriteForm
from reviewapp.models import Review


class ReviewWriteView(CreateView):
    model = Review
    form_class = WriteForm
    template_name = 'reviewapp/write.html'

    def form_valid(self, form):
        temp_review = form.save(commit=False)
        temp_review.book = Book.objects.get(pk=self.request.POST['book_pk'])
        temp_review.user = self.request.user
        temp_review.save()
        return super().form_valid(form)

    def get_success_url(self):
        from django.urls import reverse
        return reverse('bookshelfapp:review',kwargs={'pk':self.object.book.pk})
