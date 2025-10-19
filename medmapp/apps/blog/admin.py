from django.contrib import admin
from .models import Post
from ckeditor.widgets import CKEditorWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = "__all__"


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm
#     list_display = ("title", "author", "created_at")
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")