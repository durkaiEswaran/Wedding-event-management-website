from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("book/venue/<int:venue_id>/", views.book_venue, name="book_venue"),
    path("book/catering/<int:catering_id>/", views.book_catering, name="book_food"),
    path("book/stage/<int:stage_id>/", views.book_stage, name="book_stage"),
    path("book/photography/<int:photography_id>/", views.book_photography, name="book_photography"),
    path("weddingpackage/",views.wedding_package,name="wedding_package"),
    path("book/weddingpackage/<int:package_id>/", views.book_package, name="book_package"),
    path("contact/",views.contact_form,name = "contact_form"),
    path('about/',views.about,name='about'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]