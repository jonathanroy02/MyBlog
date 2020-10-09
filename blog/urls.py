from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, AddCommentView, UpdatePostView, DeletePostView, DeleteCommentView

urlpatterns = [
	#path('', views.home, name="home"),
	path('', HomeView.as_view(), name="home"), 
	path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
	path('add_post/', AddPostView.as_view(), name='add_post'),
	path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
	path('article/<int:pk>/comment/remove', DeleteCommentView.as_view(), name='delete_comment'),
	path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'), 
	path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),  
]
