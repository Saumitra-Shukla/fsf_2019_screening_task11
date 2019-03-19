from django.urls import path
from django.contrib.auth import views as auth_views
from baseapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'baseapp'

urlpatterns = [
    path('login/',  auth_views.LoginView.as_view(template_name="baseapp/login.html"),name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile,name='profile'),
    path('logout/',  auth_views.LogoutView.as_view(),name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

