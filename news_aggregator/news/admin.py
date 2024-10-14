from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publishedAt', 'source_name')  # Customize fields shown
    search_fields = ('title', 'description', 'source_name')  # Add search capability
    list_filter = ('category', 'publishedAt')  # Add filtering options
    
admin.site.register(Article, ArticleAdmin)
