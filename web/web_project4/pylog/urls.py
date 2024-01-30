"""
URL configuration for pylog project.

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("posts",include("blog.urls")),
]
urlpatterns += static(
    # URL의 접두어가 MEDIA_URL 일 때는 정적파일을 돌려준다.
    prefix=settings.MEDIA_URL,
    # 돌려줄 디럭테러는 MEDIA_ROOT를 기준으로 한다
    document_root=settings.MEDIA_ROOT,
)