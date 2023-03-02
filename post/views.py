from post.models import Author, Category, Post
from post.serializers import PostSerializer, AuthorSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.
class listCategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class createCategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        data = serializer.validated_data.get('name')
        return Response(
            {
                'data': data
            })


class detailCategoryView(generics.RetrieveAPIView):
    lookup_field = "pk"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class deleteCategoryView(generics.DestroyAPIView):
    lookup_field = "pk"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class updateCategoryView(generics.UpdateAPIView):
    lookup_field = "pk"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# AUTHOR VIEW SECTION
class listAuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class createAuthorView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class detailAuthorView(generics.RetrieveAPIView):
    lookup_field = "pk"
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class deleteAuthorView(generics.DestroyAPIView):
    lookup_field = "pk"
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class updateAuthorView(generics.UpdateAPIView):
    lookup_field = "pk"
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# POST VIEW SECTION
class listPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class createPostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class detailPostView(generics.RetrieveAPIView):
    lookup_field = "pk"
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class deletePostView(generics.DestroyAPIView):
    lookup_field = "pk"
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class updatePostView(generics.UpdateAPIView):
    lookup_field = "pk"
    queryset = Post.objects.all()
    serializer_class = PostSerializer
