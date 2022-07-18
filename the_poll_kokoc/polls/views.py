from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Poll, Question, Answer, UserAnswer, Colors, Purchase
from .forms import OneChoiceForm, QuestionsFormSet, ColorForm, PurchaseForm


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


def shop(request):
    colors = Colors.objects.all()
    balance = request.user.balance
    buy_form = PurchaseForm(
        request.POST or None,
        request.FILES or None,

    )
    if buy_form.is_valid():
        purchase = buy_form.save(commit=False)
        purchase.user = request.user
        purchase_color = buy_form.cleaned_data['color']
        purchase_type = buy_form.cleaned_data['type']
        if request.user.balance >= purchase_color.cost and not Purchase.objects.all().filter(user=request.user).filter(color=purchase_color).filter(type=purchase_type).exists():
            purchase.save()
            request.user.balance -= purchase_color.cost
            request.user.save()
            balance = request.user.balance   
            buy_form = PurchaseForm()
    context = {
        'buy_form': buy_form,
        'colors': colors,
        'balance': balance
    }
    return render(
        request,
        'polls/shop.html',
        context
    )


def profile(request):
    tests_done = Poll.objects.all().filter(user_answers__user=request.user).distinct().count()
    balance = request.user.balance
    available_login_colors = list(Purchase.objects.filter(user=request.user).filter(type='login').values_list('color_id', flat=True))
    available_background_colors = list(Purchase.objects.filter(user=request.user).filter(type='backgrnd').values_list('color_id', flat=True))
    login_color_qs = Colors.objects.filter(id__in=available_login_colors)
    background_color_qs = Colors.objects.filter(id__in=available_background_colors)
    choose_form = ColorForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user,
        login_color_qs=login_color_qs,
        background_color_qs=background_color_qs
    )
    if choose_form.is_valid():
        choose_form.save()
    context = {
        'choose_form': choose_form,
        'tests_done': tests_done,
        'balance': balance,
        'login_purchases_number': len(available_login_colors),
        'background_purchases_number': len(available_background_colors),
        'backgrnd_color': request.user.background_color.color if request.user.background_color else None
    }
    return render(
        request,
        'polls/profile.html',
        context
    )


def leaderboard(request):
    return render(request, 'polls/leaderboard.html')
