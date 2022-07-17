from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Poll, Question, Answer, UserAnswer
from .forms import OneChoiceForm, QuestionsFormSet


def index(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/index.html', context)


def take_poll(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    questions_number = Question.objects.all().filter(poll=poll_id).count()
    questions = Question.objects.all().filter(poll=poll_id)
    answers = []
    for question in questions:
        answers.append(Answer.objects.all().filter(question=question))
    QuestionFormSet = formset_factory(
        OneChoiceForm,
        extra=questions_number,
        formset=QuestionsFormSet
    )
    formset = QuestionFormSet(
        request.POST or None,
        form_kwargs={'answers_list': answers}
    )
    if formset.is_valid():
        for index, form in enumerate(formset):
            user_answer = UserAnswer(
                poll=poll,
                question=questions[index],
                user=request.user,
                answer=form.cleaned_data['answers']
            )
            user_answer.save()
        return redirect('polls:index')
    return render(request, 'polls/take_poll.html', {'formset': formset})