'''
Views for the recipe APIs.
'''

from rest_framework import (
    viewsets,
    mixins
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (Recipe, Tag)
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    '''View for manage recipe APis.'''

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]


    def get_queryset(self):
        '''Retreive recipes for authenticated user'''
        return self.queryset.filter(user=self.request.user).order_by('-id')

    # override default serialzer on calling detail endpoint on action list
    def get_serializer_class(self):
        '''Return the serializer class for request'''
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    # check that when saving recipe user is correct
    def perform_create(self, serializer):
        '''Craet a new recipe'''
        serializer.save(user=self.request.user)

class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''Manage tags ti the databae'''

    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        '''filter queryset to authenticated user'''
        return self.queryset.filter(user=self.request.user).order_by('-name')