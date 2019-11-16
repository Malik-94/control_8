from django import forms
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'description', 'images']


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'assessment']