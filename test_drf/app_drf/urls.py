from rest_framework import routers

from app_drf import views

app_router = routers.DefaultRouter()
app_router.register("app_drf", views.FoodCategoryViewSet)
