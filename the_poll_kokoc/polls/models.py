from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Poll(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Название опроса'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Название опроса'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата',
        help_text='Дата создания опроса'
    )
    reward = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Награда',
        help_text='Награда за прохождение опроса',
        blank=True
    )

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Опрос',
        help_text='Опрос, в котором находится вопрос'
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст вопроса'
    )

    def __str__(self) -> str:
        return self.text


class Answer(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Опрос',
        help_text='Опрос'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос',
        help_text='Заданный вопрос'
    )
    text = models.CharField(
        max_length=50,
        verbose_name='Текст',
        help_text='Текст ответа'
    )

    def __str__(self) -> str:
        return self.text


class UserAnswer(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='user_answers',
        verbose_name='Опрос',
        help_text='Опрос'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='user_answers',
        verbose_name='Вопрос',
        help_text='Заданный вопрос'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_answers',
        verbose_name='Пользователь',
        help_text='Пользователь, давший ответ'
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name='user_answers',
        verbose_name='Ответ',
        help_text='Ответ пользователя'
    )
