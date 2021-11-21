"""This is a test program."""
from django.db import models


class Note(models.Model):
    SCORE_CHOICE = ((1, "低"), (2, "普通"), (3, "重要"), (4, "最重要"), (5, "緊急"))
    title = models.CharField(max_length=100)
    score = models.IntegerField(choices=SCORE_CHOICE)
    text = models.TextField()
    # created_at = models.DateTimeField("作成日", auto_now_add=True)
    # updated_at = models.DateTimeField("更新日", auto_now=True)
    def __str__(self):
        return self.Note
