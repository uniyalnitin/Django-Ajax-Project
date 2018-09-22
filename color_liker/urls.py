from django.conf.urls import url
from django.urls import path
from color_liker import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("", views.ColorList.as_view(),name= "color_list"),
	path('like_color_/<int:color_id>/', views.toggle_color_like,name="toggle_color_like"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)