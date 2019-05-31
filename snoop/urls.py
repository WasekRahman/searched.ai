from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    SawPostListView,
    SawPostDetailView,
    SawPostCreateView,
    SawPostUpdateView,
    SawPostDeleteView,
    UserPostListView,
    matched,
    announcements,
)

urlpatterns = [ 
 
 
	path('', PostListView.as_view(), name='snoop-home'),
	path('searchd/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('searchd/report/', PostCreateView.as_view(), name='post-create'),
	path('searchd/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('searchd/<int:pk>/delete/', PostUpdateView.as_view(), name='post-delete'),
	path('searchd/suspect/<int:pk>/', SawPostDetailView.as_view(), name='sawpost-details'),
	path('searchd/suspect/report/', SawPostCreateView.as_view(), name='sawpost-create'),
    path('about/', views.about, name='snoop-about'),
    path('my_matches/', views.matched, name='matched'),
    path('announcements/', views.announcements, name='announcements'),
    path('myposts/', UserPostListView.as_view(), name='user-posts'),
    path('suspects/',  SawPostListView.as_view(), name='snoop-suspect'),
  	path('accounts/', include('allauth.urls')),
  	path('searchd/suspect/<int:pk>/update/', SawPostUpdateView.as_view(), name='sawpost-update'),
    path('searchd/suspect/<int:pk>/delete/', SawPostDeleteView.as_view(), name='sawpost-delete'),
    

    
     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)