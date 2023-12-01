from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import FormMixin

from bookapp.models import Book
from reviewapp.forms import WriteForm
from reviewapp.models import Review
from django.urls import reverse


class ReviewWriteView(CreateView):
    model = Review
    form_class = WriteForm
    template_name = 'reviewapp/write.html'

    def form_valid(self, form):
        temp_review = form.save(commit=False)
        temp_review.book = Book.objects.get(pk=self.request.POST['book_pk'])
        temp_review.writer = self.request.user
        temp_review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reviewapp:review',kwargs={'pk':self.object.book.pk})


class ReviewDeleteView(DeleteView):
    model = Review
    context_object_name = 'target_review'
    template_name = 'reviewapp/delete.html'

    def get_success_url(self):
        return reverse('reviewapp:review',kwargs={'pk':self.object.book.pk})


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = WriteForm
    context_object_name = 'target_review'
    template_name = 'reviewapp/update.html'

    def get_success_url(self):
        return reverse('reviewapp:review',kwargs={'pk':self.object.book.pk})



class ReviewDetailView(DetailView, FormMixin):
    model = Book
    form_class = WriteForm
    context_object_name = 'target_book'
    template_name = 'bookshelfapp/review.html'
