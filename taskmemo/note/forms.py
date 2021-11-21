from django.forms import ModelForm
from .models import Note

class NoteForm(ModelForm):
    # django側から利用する情報を記述 →情報の補足を行っている

    # modelフォームにあるがオーバーライドする為に記述
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            # フォームのレイアウトを整える為のclass="form-control" を付与する処理
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Note
        #入力項目から作成日時、更新日時を除外
        # exclude = ('created_at','updated_at',)
        fields = ['title', 'score', 'text']
