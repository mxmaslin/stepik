from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer
from django.contrib.auth import authenticate


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class AskForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text',)


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text', 'question',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError('Username is empty',
                                        code='validation_error')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError('Password is empty',
                                        code='validation_error')
        return password

    def save(self):
        auth = authenticate(**self.cleaned_data)
        return auth
