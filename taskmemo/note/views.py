#pylint: disable=E1103
"""noteのviews"""
# getでとってくるかidで見つからない場合はdjangoエラー画面ではなく404画面を表示させるimport
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import Note
from .forms import NoteForm

# 一覧画面のview
class IndexView(generic.ListView):
    model = Note
    # 一覧表示時の1ページでの最大表示数
    paginate_by = 5

# 詳細画面のview
class DetailView(generic.DetailView):
    model = Note

# 登録画面のview
class CreateView(generic.CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('note:note_list')

# 更新画面のview
class UpdateView(generic.UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('note:note_list')

# 削除処理のview
class DeleteView(generic.DeleteView):
    model = Note
    success_url = reverse_lazy('note:note_list')
