from django.contrib import admin
from django.urls import path, include
from feeds import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/feeds/', include("feeds.urls")),
    path('api/v1/users/', include("users.urls")),
    path('api/v1/reviews/', include("reviews.urls"))
]
