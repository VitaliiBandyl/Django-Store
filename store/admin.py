from django import forms
from django.contrib import admin

from .models import Category, Product, ProductShot, Rating, Reviews
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductAdminForm(forms.ModelForm):
    """CKEditor form"""
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'


class ReviewInline(admin.StackedInline):
    """Reviews inline view"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email', 'product')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Django admin category CRUD form"""
    list_display = ('name', 'url')
    list_display_links = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Django admin product CRUD form"""
    list_display = ('title', 'category', 'year', 'country', 'price', 'availability', 'new',
                    'top_selling', 'discount', 'created', 'updated')
    list_filter = ('category', 'year', 'country', 'new', 'availability', 'top_selling')
    search_fields = ('title', 'category__name')
    inlines = [ReviewInline]
    form = ProductAdminForm
    save_on_top = True
    save_as = True
    list_editable = ('price', 'availability', 'new', 'top_selling', 'discount')
    fieldsets = (
        (None, {
            'fields': (('title', 'url'),)
    }),
      (None, {
            'fields': ('description', 'image')
    }),
        (None, {
            'fields': (('category', 'country', 'year'),)
    }),
        (None, {
            'fields': (('price', 'discount'),)
    }),
        (None, {
            'fields': (('draft', 'new', 'availability', 'top_selling'),)
        }),
    )


@admin.register(ProductShot)
class ProductShotAdmin(admin.ModelAdmin):
    """Django admin product shots CRUD form"""
    list_display = ('title', 'product')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Django admin reviews CRUD form"""
    list_display = ('name', 'email', 'product')
    readonly_fields = ('name', 'email', 'product')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Django admin rating CRUD form"""
    list_display = ('product', 'star', 'ip')
