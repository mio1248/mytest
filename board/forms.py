from django import forms

from .models import BoardPost


class BoardPostForm(forms.ModelForm):
    class Meta:
        model = BoardPost
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '제목을 입력해 주세요.',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '내용을 입력해 주세요.',
                    'rows': 8,
                }
            ),
        }
