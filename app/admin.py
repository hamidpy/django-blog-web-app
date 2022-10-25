from django.contrib import admin
from .models import *


class TagTublerInline(admin.TabularInline):
    model = Tag


class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerInline]
    list_display = ['title','author','date','status','section','Main_post']
    list_editable = ['status','section','Main_post']
    search_fields = ['title','section']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
