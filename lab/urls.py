from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .models import Cars,Game,Subscriptions,gadgets
from django.contrib.auth import views as auth_views






urlpatterns = [
path('register/', views.register, name='register'),  # Регистрация
path('login/', auth_views.LoginView.as_view(template_name='lab/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Выход
path('accounts/profile/', views.profile, name='profile'),  # Страница профиля
path ('', views.index, name='index'),
path ('about/', views.about, name='about'),
path ('tarif/', views.tar, name='tar'),
path ('yslovia/', views.ysl, name='ysl'),
path ('review/', views.rev,name='rev'),
path ('car/<int:car_id>/',views.cars, name='car_detail'),
path ('subs/<int:sub_id>/',views.subs, name='sub_det'),
path ('games/<int:game_id>/',views.games, name='game_det'),
path ('gads/<int:gad_id>/',views.gads, name='gad_det'),
path ('game/', views.game,name='game'),
path ('gadgets/', views.gad,name='gadgets'),
path ('sub/', views.sub,name='sub'),
path ('kar/', views.kar,name='kar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)