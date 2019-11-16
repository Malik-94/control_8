from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'
    model = Product



class ProductView(DetailView):
    template_name = 'products/product_detail.html'
    pk_url_kwarg = 'pk'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/producrt_update.html'
    form_class = ProductForm
    context_object_name = 'obj'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    context_object_name = 'obj'
    success_url = reverse_lazy('webapp:index')