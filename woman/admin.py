from django.contrib import admin
from woman.models import Woman, Category


class AdminCategory(admin.ModelAdmin):
    # List of category fields
    # ('id', 'name')

    # List of categories form
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

    class Meta:
        model = Category


class AdminWomen(admin.ModelAdmin):
    # List of Women model fields
    # ('id', 'title', 'content', 'time_create', 'time_update', 'is_published', 'cat')

    # List of woman form
    list_display = ('title', 'content', 'time_create', 'time_update', 'is_published', 'cat')
    search_fields = ('title',)
    list_filter = ('cat',)

    class Meta:
        model = Woman


admin.site.register(Woman, AdminWomen)
admin.site.register(Category, AdminCategory)
