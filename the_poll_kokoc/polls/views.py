from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Poll, Question, Answer, UserAnswer
from .forms import OneChoiceForm, QuestionsFormSet


User = get_user_model()


def index(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/index.html', context)


@login_required
def take_poll(request, poll_id):
    if UserAnswer.objects.all().filter(poll=poll_id).exists():
        return redirect('polls:index')
    poll = Poll.objects.get(id=poll_id)
    questions_number = Question.objects.all().filter(poll=poll_id).count()
    questions = Question.objects.all().filter(poll=poll_id)
    answers = []
    for question in questions:
        answers.append(Answer.objects.all().filter(question=question))
    QuestionFormSet = formset_factory(
        OneChoiceForm,
        extra=0,
        min_num=questions_number,
        validate_min=True,
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
        request.user.balance += poll.reward
        request.user.save()
        return redirect('polls:index')
    return render(
        request,
        'polls/take_poll.html',
        context={
            'formset': formset,
            'question_data': zip(formset, questions),
            'poll': poll
        }
    )


def leaderboard(request):
    return render(request, 'polls/leaderboard.html')
