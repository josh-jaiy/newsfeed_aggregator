import requests
from django.shortcuts import render
from .models import Article

# Fetch articles from NewsAPI
def get_news(category):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        'apiKey': '0842c69478d1447db5608999407ac556',  # Replace with your valid API key
        'country': 'us',
        'category': category,
        'pageSize': 10,  # Set the number of articles to fetch
    }
    response = requests.get(url, params=params)
    return response.json()

# Save fetched articles into the database
def save_articles(articles, category):
    for article in articles:
        # Check if the article already exists based on the title
        if not Article.objects.filter(title=article['title']).exists():
            new_article = Article(
                title=article['title'],
                description=article['description'],
                url=article['url'],
                image_url=article.get('urlToImage'),  # Use get to avoid errors if the field is missing
                published_at=article['publishedAt'],
                source_name=article['source']['name'],
                category=category  # Save the category for the article
            )
            new_article.save()

# Display news articles with search and category filtering
def news(request):
    # Get the category and search query from the request, default to 'all'
    category = request.GET.get('category', 'all')
    search_query = request.GET.get('q', '')
    

    # If a specific category is selected, filter by category
    if category != 'all':
        articles = Article.objects.filter(category__iexact=category)
    else:
        articles = Article.objects.all()

    # Apply search query filter if provided
    if search_query:
        articles = articles.filter(title__icontains=search_query)

    # Get distinct categories for the dropdown/filter
    categories = Article.objects.values_list('category', flat=True).distinct()

    return render(request, 'news.html', {
        'categories': categories,
        'articles': articles,
        'category': category,
        'search_query': search_query,
    })
    #Developed by yisanet@gmail.com -->
# List articles and provide category filtering
def article_list(request):
    # Get the selected category from the query string
    selected_category = request.GET.get('category', 'All')

    # Fetch distinct categories for the dropdown
    categories = Article.objects.values_list('category', flat=True).distinct()

    # Filter articles based on the selected category
    if selected_category == 'All':
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(category=selected_category)

    context = {
        'articles': articles,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'article_list.html', context)
