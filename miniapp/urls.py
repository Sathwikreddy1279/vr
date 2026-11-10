from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    # path('home/', views.code_execution_view, name='code_execution_view'),
    path('home/',views.code_execution_view,name="code_execution_view"),
    path('loadimages/',views.loadimages,name='loadimages'),
    path('collection/', views.loadimages, name='collection'),
    path('home/',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    path('home/', views.runcode_view, name='runcode'),
    path('profile/', views.profile, name='profile'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('button_action/', views.button_action, name='button_action'),
    path('contact/', views.contact, name='contact'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

