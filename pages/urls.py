from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Recipes.as_view(), name=""),
    path("register", views.register, name="register"),
    path("my-login", views.my_login, name="my-login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("user-logout", views.user_logout, name="user-logout"),
    path("my-profile", views.my_profile, name="my-profile"),
    path("recipe-creation", views.recipe_creation, name="recipe-creation"),
    path('delete-recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('edit-recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('like-recipe/<int:recipe_id>/', views.like_recipe, name='like-recipe'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('my-likes/', views.LikedRecipes.as_view(), name='my-likes'),
    path('friends/', views.friends_list, name='friends_list'),
    path('follow-user/<int:user_id>/', views.follow_user, name='follow_user'),
    path('user/<int:user_id>/', views.user_profile, name='user-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)