from django.shortcuts import get_object_or_404
from rest_framework import permissions, filters, viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from .models import Post, Comment, Follow, Group
from .permissions import IsAuthorOrReadOnlyPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnlyPermission)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnlyPermission)

    def get_queryset(self):
        queryset = Comment.objects.filter(
            post=get_object_or_404(Post, pk=self.kwargs.get('post_id')))
        print(queryset)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=get_object_or_404(Post,
                                               pk=self.kwargs.get('post_id')))


class FollowViewSet(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = serializers.FollowSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnlyPermission)
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
