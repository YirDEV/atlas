
# import your folders to find your app files
from django.contrib import admin
from django.urls import path
from references import views as ref_views

# Create your App URLS here
# Here is where you call your view and its respective views.py functions
urlpatterns = [
    path('admin/', admin.site.urls),
    path('references/',ref_views.references_db),
]
