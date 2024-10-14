from django.db import models

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('technology', 'Technology'),
        ('business', 'Business'),
        ('sports', 'Sports'),
        ('health', 'Health'),
        # You can add more categories if necessary
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    urlToImage = models.URLField(null=True, blank=True)  # Optional image URL
    publishedAt = models.DateTimeField()  # Publication date
    source_name = models.CharField(max_length=255, default='Unknown')  # Source name
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Category choices

    def __str__(self):
        return self.title
