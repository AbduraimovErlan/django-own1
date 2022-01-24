import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="image/%Y/%m/%d?")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    def was_published_recently(self):
        return self.time_create >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['time_create', 'title']




class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']




class Comment(models.Model):
    title = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст коментария', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "комментария"
        verbose_name_plural = "комментарии"
