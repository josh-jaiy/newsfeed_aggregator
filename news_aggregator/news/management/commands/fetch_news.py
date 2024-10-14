import requests
from django.core.management.base import BaseCommand
from news.models import Article  # Adjust the import based on your model

from news.views import get_news, save_articles


class Command(BaseCommand):
    help = 'Fetch the latest news from NewsAPI and store it in the database'

    def handle(self, *args, **kwargs):
        url = "https://newsapi.org/v2/top-headlines"
        api_key = '0842c69478d1447db5608999407ac556'  # Replace with your NewsAPI key
        country = 'us'
        categories = ['technology', 'business', 'sports', 'health']  # List of categories to fetch
        page_size = 10

        for category in categories:
            self.stdout.write(f'Fetching {category} news...')

            params = {
                'apiKey': api_key,
                'country': country,
                'category': category,
                'pageSize': page_size,
            }
            response = requests.get(url, params=params)
            news_data = response.json()

            if news_data.get('status') == 'ok':
                articles = news_data.get('articles', [])
                for article_data in articles:
                    # Create or update Article objects based on your model
                    article, created = Article.objects.update_or_create(
                        title=article_data['title'],
                        defaults={
                            'description': article_data['description'],
                            'url': article_data['url'],
                            'urlToImage': article_data['urlToImage'],
                            'publishedAt': article_data['publishedAt'],
                            'source_name': article_data['source']['name'],  # Ensure your model has this field
                            'category': category,  # Add category here
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Article "{article.title}" added.'))
                    else:
                        self.stdout.write(f'Article "{article.title}" updated.')

            else:
                self.stdout.write(self.style.ERROR(f'Failed to fetch {category} news.'))

        self.stdout.write("All categories fetched and saved.")
