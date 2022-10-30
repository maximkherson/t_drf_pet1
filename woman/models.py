from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # def __str__(self):
    #     return self.name


class Woman(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'women'
        verbose_name = 'Woman'
        verbose_name_plural = 'Women'

    # def __str__(self):
    #     return self.title
