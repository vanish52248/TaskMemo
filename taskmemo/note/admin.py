from django.contrib import admin
# modelを認識させるimport
from .models import Note

# Noteモデルを管理サイトに認識させる
admin.site.register(Note)