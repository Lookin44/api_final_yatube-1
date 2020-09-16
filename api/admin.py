from django.contrib import admin

from .models import Post, Comment, Group, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author", "group")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "post", "text", "created")
    search_fields = ("text",)
    list_filter = ("created",)
    empty_value_display = '-пусто-'


admin.site.register(Comment, CommentAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    search_fields = ("title",)
    empty_value_display = '-пусто-'


admin.site.register(Group, GroupAdmin)


class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "following")
    empty_value_display = '-пусто-'


admin.site.register(Follow, FollowAdmin)
