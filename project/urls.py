"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from everapp import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='home'),
    path('home/', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('add_property/', views.add_property, name='add_property'), 
    path('property-search/', views.property_search, name='property_search_view'),    
    path('portfolio/', views.portfolio, name="portfolio"),
    path('set_appointment/', views.set_appointment, name='set_appointment'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('reviews_list/', views.reviews_list, name='reviews_list'),
    path('faq/', views.faq, name='faq'), 
    path('property/<int:pk>/', views.property_link, name='property_detail'), 
    path('contact_form/', views.send_email, name="contact_form"),
   
    
    
    path('logout/',views.logout_user,name="logout"),
   path('activation_sent/', views.activation_sent, name='activation_sent'),
    path('registro/', views.registro_usuario, name='registro'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login/', views.login_user, name='login'),
    

    
    ######################################  RESTAURANTS #########################################
    path('restaurant_recommendation_list/', views.restaurant_recommendation_list, name='restaurant_recommendation_list'),
    path('restaurant/<int:pk>/', views.restaurant_recommendation_link_to_share, name='restaurant_recommendation_detail'),
    path('restaurant/new/', views.restaurant_recommendation_create, name='restaurant_recommendation_create'),
    path('restaurant/<int:pk>/edit/', views.restaurant_recommendation_edit, name='restaurant_recommendation_edit'),
    
    ####################################  bars #########################
    path('bar_recommendation_list/', views.bar_recommendation_list, name='bar_recommendation_list'),
    path('bar/<int:pk>/', views.bar_recommendation_link_to_share, name='bar_recommendation_detail'),
    path('bar/new/', views.bar_recommendation_create, name='bar_recommendation_create'),
    path('bar/<int:pk>/edit/', views.bar_recommendation_edit, name='bar_recommendation_edit'),
    
    ####################################  TOURS  #########################
    path('tour_recommendation_create', views.tour_recommendation_create, name='tour_recommendation_create'),
    path('tour_recommendation_list/', views.tour_recommendation_list, name='tour_recommendation_list'),
    path('tour/<int:pk>/', views.tour_recommendation_link_to_share, name='tour_recommendation_detail'),  
    path('tour/<int:pk>/edit/', views.tour_recommendation_edit, name='tour_recommendation_edit'),
    
    ####################################  Gallery  #########################
    path('gallery_recommendation_create', views.gallery_recommendation_create, name='gallery_recommendation_create'),
    path('gallery_recommendation_list/', views.gallery_recommendation_list, name='gallery_recommendation_list'),
    path('gallery/<int:pk>/', views.gallery_recommendation_link_to_share, name='gallery_recommendation_detail'),  
    path('gallery/<int:pk>/edit/', views.gallery_recommendation_edit, name='gallery_recommendation_edit'),
    
    path('web_developer_puerto_vallarta/', views.author, name='web_developer_puerto_vallarta'),
    path('attorney/', views.attorney, name='attorney'),
    



    
    

    
    

    
]


#ESTO LO ESTAMOS HACIENDO PARA QUE MI SITIO WEB PUEDA ABRIR LAS IMAGENES QUE SUBO CON form, ESTO VA ACOMPAÑADO DE LA CONFIGURACION MEDIA Y ROOT DE settings.py

#CONFIGURACION PARA VISUALIZAR IMAGENES EN DJANGO
if settings.DEBUG: #CUANDO DEJO ESTO ASI SIGNIFICA QUE SI ES True
    from django.conf.urls.static import static
    #urlpatterns ES TODAS LAS url QUE TENGO CONFIGURADAS ARRIBA Y CON EL += LE ESTOY CONCATENANDO UNA NUEVA url 
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #CON ESTO YA ME VA ABRIR Django LA IMAGEN



