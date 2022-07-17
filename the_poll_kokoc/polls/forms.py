from django import forms
from django.forms import BaseFormSet

from .models import Question


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