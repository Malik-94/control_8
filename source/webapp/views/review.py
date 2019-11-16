from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import  CreateView, UpdateView, DeleteView
from webapp.forms import ProductReviewForm
from webapp.models import Product, Review


class ReviewForProductCreateView(CreateView):
    template_name = 'review/review_create.html'
    form_class = ProductReviewForm

    def form_valid(self, form):
        user = self.request.user
        product_pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_pk)
        product.reviews.create(user=user, **form.cleaned_data)
        return redirect('webapp:product_view', pk=product_pk)


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review/review_update.html'
    form_class = ProductReviewForm
    context_object_name = 'obj'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(DeleteView):
    template_name = 'review/review_delete.html'
    model = Review
    context_object_name = 'obj'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})