from django.contrib import admin
from .models import Post,comments,Like,PostImages,Rating


class PostImageAdmin(admin.StackedInline):
    model = PostImages

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

admin.site.register(comments)
admin.site.register(Like)
admin.site.register(Rating)