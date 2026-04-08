from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class PizzaLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'placeholder': '아이디를 입력하세요',
                'autocomplete': 'username',
                'autofocus': True,
            }
        ),
    )
    password = forms.CharField(
        label='비밀번호',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 입력하세요',
                'autocomplete': 'current-password',
            }
        ),
    )


class PizzaSignupForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'placeholder': '사용하실 아이디를 입력하세요',
                'autocomplete': 'username',
            }
        ),
    )
    password1 = forms.CharField(
        label='비밀번호',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 입력하세요',
                'autocomplete': 'new-password',
            }
        ),
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 한 번 더 입력하세요',
                'autocomplete': 'new-password',
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = '영문, 숫자, 일부 특수문자만 사용할 수 있습니다.'
        self.fields['password1'].help_text = '비밀번호는 너무 짧거나 단순하면 사용할 수 없습니다.'
        self.fields['password2'].help_text = '위와 같은 비밀번호를 다시 입력해 주세요.'
