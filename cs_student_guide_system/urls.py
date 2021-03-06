
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')), 
    path('', include('student_panel.urls')), 
    path('course/', include('course_system.urls')), 
    path('professor/', include('professor_panel.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)