from rest_framework import serializers
from booksale.models import Book, Category
from django.contrib.auth.models import User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Book
        fields = ('title', 'published', 'price', 'stock',
                  'cat', 'owner')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    book_set = BookSerializer(read_only=True, many=True)
    categ = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ('categ','book_set')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'book')