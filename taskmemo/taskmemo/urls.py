from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # アプリごとのurls.pyを読み込む設定
    path('note/', include('note.urls'))
]
