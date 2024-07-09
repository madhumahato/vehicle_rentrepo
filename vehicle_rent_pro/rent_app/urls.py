from django.urls import path
from  rent_app import views
urlpatterns = [
    path("index/", views.index, name='index'),
    path("contact/", views.contact_form, name='contact'),
    path("singup_form/", views.signup_up_form, name='singup_form'),
    path("login_form/", views.login_form, name='login_form'),
    path("logout_form/", views.logout_form, name='logout_form'),

]
