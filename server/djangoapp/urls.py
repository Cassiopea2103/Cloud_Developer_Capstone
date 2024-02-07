from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
 
    # About Us :
    path ( route = 'about' , view = views.about_us , name = "about") ,
    # Contact Us :
    path ( route = 'contact', view = views.contact_us, name="contact" ) ,

    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name="home"),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)