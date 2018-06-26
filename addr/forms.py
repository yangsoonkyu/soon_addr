from django import forms

from .models import Friend, Memo

class FriendForm(forms.ModelForm):

    class Meta:
        model = Friend
        fields = ('name', 'phon_number_1', 'phon_number_2', 'e_mail',)

class MemoForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ('text',)