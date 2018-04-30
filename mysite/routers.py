
from rest_framework.routers import DefaultRouter

from article.viewsets import ArticleViewset

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'article', ArticleViewset)
