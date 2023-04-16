from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
)
from django.urls import path, include
from api.views import *

urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:category_id>/', CategoryDetail.as_view()),
    path('categories/<int:category_id>/products/', product_list_by_category_id),

    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),

    path('news/', NewsList.as_view()),
    path('images/', ImageList.as_view()),
    path('comments/', CommentList.as_view()),

    path('user/', user_by_username),
    path('sign-up/', sign_up_user),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verify-token/', TokenVerifyView.as_view(), name='token_verify')
]
