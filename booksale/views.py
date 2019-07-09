from booksale.models import Book, Category
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from booksale.models import Book, Category
from booksale.permissions import IsSellerOrReadOnly
from booksale.serializers import BookSerializer, CategorySerializer

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'category': reverse('category-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format)
    })


class BookViewSet(viewsets.ModelViewSet):
    """

    retrieve:
    Return the given book.

    list:
    Return a list of all the existing books.

    create:
    Create a new book instance.

    update:
    Updates the instance with the provided id

    delete:
    Destroys the instance with the provided id

    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSellerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Return the given category with all of its books.

    list:
    Return a list of all the existing categories.

    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
