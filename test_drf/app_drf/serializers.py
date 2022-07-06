from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import FoodCategory, Food


class FoodSerializer(ModelSerializer):
    additional = SlugRelatedField(many=True, read_only=True, slug_field="internal_code")

    class Meta:
        model = Food
        fields = (
            "internal_code",
            "code",
            "name_ru",
            "description_ru",
            "description_en",
            "description_ch",
            "is_vegan",
            "is_special",
            "cost",
            "additional",
        )


class FoodListSerializer(ModelSerializer):
    foods = FoodSerializer(source="food", many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ("id", "name_ru", "name_en", "name_ch", "order_id", "foods")
