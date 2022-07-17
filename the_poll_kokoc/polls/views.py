from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Poll, Question, Answer, UserAnswer
from .forms import OneChoiceForm


def index(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/index.html', context)

def take_poll(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    question = Question.objects.get(poll=poll_id)
    answers = Answer.objects.all().filter(poll=poll_id)
    form = OneChoiceForm(
        request.POST or None,
        answers_qs=answers)
    if form.is_valid():
        answer = form.cleaned_data['answers']
        user_answer = UserAnswer(
            poll=poll,
            question=question,
            user=request.user,
            answer=answer
        )
        user_answer.save()
        return redirect('polls:index')
    return render(
        request,
        'polls/take_poll.html',
        {'form': form}
    )
    #questions_amount = Question.objects.all().filter(poll=poll_id).count()
    #QuestionFormSet = formset_factory(OneChoiceForm, extra = questions_amount)
    #formset = QuestionFormSet()
    #if request.method == 'POST':
        #formset = QuestionFormSet(request.POST)
        #if formset.is_valid():
            #UserAnswer.objects.create(
                #poll = poll,
                #question = 
            #)
