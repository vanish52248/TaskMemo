from django.urls import path
from .import views

app_name = 'note'
# <int:pk>はpathにパラメータを含ませる記述
urlpatterns = [
    # 一覧画面のview
    path('', views.IndexView.as_view(), name="note_list"),
    # 詳細画面のview idごとに内容違う
    path('detail/<int:pk>/', views.DetailView.as_view(), name="note_detail"),
    # 登録画面のview
    path('create/', views.CreateView.as_view(), name="note_create"),
    # 更新画面のview(更新) idごとに内容違う
    path('update/<int:pk>/', views.UpdateView.as_view(), name="note_update"),
    # 削除画面のview idごとに内容違う
    path('delete/<int:pk>/', views.DeleteView.as_view(), name="note_delete"),
]