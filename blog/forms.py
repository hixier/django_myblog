from django.forms import ModelForm
from .models import Comment


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', ]







