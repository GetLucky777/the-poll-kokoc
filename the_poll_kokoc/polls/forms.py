from django import forms
from django.forms import BaseFormSet
from django.contrib.auth import get_user_model

from .models import Question, Purchase

User = get_user_model()


class OneChoiceForm(forms.Form):
    answers = forms.ModelChoiceField(
        queryset=Question.objects.none(),
        widget=forms.RadioSelect,
        empty_label=None
    )

    def __init__(self, *args, **kwargs):
        answers_qs = kwargs.pop('answers_qs')
        qs_list = kwargs.pop('answers_list')
        super(OneChoiceForm, self).__init__(*args, **kwargs)
        self.fields['answers'].queryset = answers_qs


class QuestionsFormSet(BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super(QuestionsFormSet, self).get_form_kwargs(index)
        kwargs['answers_qs'] = kwargs['answers_list'][index]
        return kwargs


class ColorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'login_color',
            'background_color'
        )

    def __init__(self, *args, **kwargs):
        login_color_qs = kwargs.pop('login_color_qs')
        background_color_qs = kwargs.pop('background_color_qs')
        super(ColorForm, self).__init__(*args, **kwargs)
        if login_color_qs:
            self.fields['login_color'].queryset = login_color_qs
        else:
            self.fields.pop('login_color')
        if background_color_qs:
            self.fields['background_color'].queryset = background_color_qs
        else:
            self.fields.pop('background_color')


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = (
            'color',
            'type'
        )
