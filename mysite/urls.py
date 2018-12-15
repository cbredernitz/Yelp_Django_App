
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('yelp/')),
    url(r'^admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
         name='logout'),
    url(r'^yelp/', include('yelp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)