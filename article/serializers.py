from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    detail_url = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
