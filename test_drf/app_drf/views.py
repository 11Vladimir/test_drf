from django.db.models import Prefetch
from rest_framework import permissions
from rest_framework import viewsets

from .models import Food, FoodCategory
from .serializers import FoodListSerializer, FoodSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
            Prefetch("food", queryset=Food.objects.filter(is_publish=True))
        )
        return queryset


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]
