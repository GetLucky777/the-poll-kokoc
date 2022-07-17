from django import forms

from .models import Question, UserAnswer


#class OpenQuestionForm(forms.Form):
    # answers = forms.Textarea(
        # label='Напишите ваш ответ в поле'
    # )


class OneChoiceForm(forms.Form):
    answers = forms.ModelChoiceField(
        queryset=Question.objects.none(),
        widget=forms.RadioSelect
    )
    
    def __init__(self, *args, **kwargs):
        answers_qs = kwargs.pop('answers_qs')
        super(OneChoiceForm, self).__init__(*args, **kwargs)
        self.fields['answers'].queryset = answers_qs



# class MultipleChoiceForm(forms.Form):
    # answers = forms.CheckboxSelectMultiple(
        # label='Выберите несколько вариантов ответа'
    # )
