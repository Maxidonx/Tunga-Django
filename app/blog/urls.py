"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import BlogPostViewSet
from comments.views import CommentViewSet
from register.views import RegisterView, LoginView
from user.views import UserProfileView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from register.views_html import register_page, login_page
from post.views_html import blog_index, blog_detail, blog_create, blog_edit, blog_delete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView






router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/login/', LoginView.as_view(), name='login'),
    # path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/posts/<int:post_id>/comments/', CommentViewSet.as_view ({'get': 'list'}), name='post-comments'),
]

#Register HTML frontend views
urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    path('register/', register_page, name='register-page'),
    path('login/', login_page, name='login-page'),
]

#Post HTML frontend views
urlpatterns += [
    path('', blog_index, name='post-list-page'),
    path('post/<int:post_id>/', blog_detail, name='post-detail-page'),
    path('post/create/', blog_create, name='post-create'),
    path('post/<int:post_id>/edit/', blog_edit, name='post-edit'),
    path('post/<int:post_id>/delete/', blog_delete, name='post-delete'),
]