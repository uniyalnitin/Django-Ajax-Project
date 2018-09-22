from django.conf.urls import url
from django.urls import path
from color_liker import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("", views.ColorList.as_view(),name= "color_list"),
	path('like_color_/<int:color_id>/', views.toggle_color_like,name="toggle_color_like"),
	# path('search_colors/', views.submit_color_search_from_ajax, name = "search_color_ajax"),
	path('get_color_ajax/',views.get_color_ajax, name="get_color_ajax"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)