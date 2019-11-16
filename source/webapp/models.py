from django.conf import settings
from django.db import models
from django.db.models import Model

CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)


class Products(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='Название')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория')
    description = models.CharField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    images = models.ImageField(null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                             verbose_name='Пользователь', related_name='orders')
    product = models.ForeignKey('Products', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Товар')

    review_text = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Текст отзывы')
    assessment = models.FloatField(verbose_name='оценка')

    def __str__(self):
        return "{} / {}".format(self.user, self.product, self.assessment)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
