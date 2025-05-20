from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

def root_view(request):
    return JsonResponse({"message": "Payments API is running."})

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('payments.urls')),
]
