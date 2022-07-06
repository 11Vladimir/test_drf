from django.test import TestCase

from .models import FoodCategory, Food


class FoodTestCase(TestCase):
    def setUp(self):
        FoodCategory.objects.create(name_ru="Напитки")
        FoodCategory.objects.create(name_ru="Закуски")
        FoodCategory.objects.create(name_ru="Горячее")

        Food.objects.create(
            category_id=1,
            name_ru="Морс",
            code=5,
            internal_code=100,
            cost=12.0,
            is_publish=True,
        )

        Food.objects.create(
            category_id=1,
            name_ru="Чай",
            code=5,
            internal_code=200,
            cost=12.0,
            is_publish=False,
        )

        Food.objects.create(
            category_id=3,
            name_ru="Бургер",
            code=5,
            internal_code=300,
            cost=12.0,
            is_publish=True,
        )

        Food.objects.create(
            category_id=3,
            name_ru="Каша",
            code=5,
            internal_code=400,
            cost=12.0,
            is_publish=False,
        )

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)

    def test_food_category(self):
        response = self.client.get("/api/v1/foods/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 2)

        self.assertEqual(len(response.data[0]["foods"]), 1)
