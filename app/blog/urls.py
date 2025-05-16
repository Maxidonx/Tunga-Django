
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from post.views import BlogPostViewSet
from comments.views import CommentViewSet
from register.views import RegisterView, LoginView
from user.views import UserProfileView
from django.contrib.auth.views import LogoutView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import dashboard
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from register.views_html import login_page, register_page
from post.views_html import blog_index, blog_detail, blog_create, blog_edit, blog_delete
from comments.views_html import comment_edit, comment_delete
from comments.views_html import comment_create, comment_edit, comment_delete, comment_like_toggle
from post.views_html import post_like_toggle
from user.views_html import profile_edit, profile_view
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



schema_view = get_schema_view(
   openapi.Info(
      title="My Blog API",
      default_version='v1',
      description="API documentation for Blog project",
      terms_of_service="https://www.google.com/policies/terms/",
      authentication_classes=[],
      contact=openapi.Contact(email="contact@myblog.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/posts/<int:post_id>/comments/', CommentViewSet.as_view ({'get': 'list'}), name='post-comments'),
    


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

#Register/login/logout HTML frontend views
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('register/', register_page, name='register-page'),
    path('login/', login_page, name='login-page'),
    path('logout/', LogoutView.as_view(next_page='login-page'), name='logout'),

]

#Post HTML frontend views
urlpatterns += [
    path('', blog_index, name='post-list-page'),
    path('post/<int:post_id>/', blog_detail, name='post-detail-page'),
    path('post/create/', blog_create, name='post-create'),
    path('post/<int:post_id>/edit/', blog_edit, name='post-edit'),
    path('post/<int:post_id>/delete/', blog_delete, name='post-delete'),
    path('post/<int:post_id>/like/', post_like_toggle, name='post-like-toggle'),
]


#Comment HTML frontend views
urlpatterns += [
    path('post/<int:post_id>/comment/', comment_create, name='post-comment-create'),
    path('comment/<int:comment_id>/edit/', comment_edit, name='comment-edit'),
    path('comment/<int:comment_id>/delete/', comment_delete, name='comment-delete'),
    path('comment/<int:comment_id>/like/', comment_like_toggle, name='comment-like-toggle'),
    path('post/<int:post_id>/like/', post_like_toggle, name='post-like-toggle'),
]




# User HTML frontend views
urlpatterns += [
    path('profile/', profile_view, name='profile-page'),
    path('profile/edit/', profile_edit, name='profile-edit'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
