from django.db import models
from django.contrib.auth.models import AbstractUser


class Colors(models.Model):
    GRAY = 'bg-secondary'
    BLUE = 'bg-primary'
    RED = 'bg-danger'
    GREEN = 'bg-success'
    USER_COLOR_CHOICES = [
        (GRAY, 'Черный'),
        (BLUE, 'Синий'),
        (RED, 'Красный'),
        (GREEN, 'Зеленый')
    ]

    color = models.CharField(
        max_length=20,
        choices=USER_COLOR_CHOICES,
        verbose_name='Цвет',
        help_text='Цвет'
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Цена',
        help_text='Цена покупки цвета'
    )

    def __str__(self):
        return self.get_color_display()


class User(AbstractUser):
    balance = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00,
        verbose_name='Баланс',
        help_text='Баланс юзера'
    )
    login_color = models.ForeignKey(
        Colors,
        on_delete=models.CASCADE,
        related_name='users_login_color',
        null=True,
        blank=True,
        verbose_name='Цвет логина',
        help_text='Цвет рамки логина'
    )
    background_color = models.ForeignKey(
        Colors,
        on_delete=models.CASCADE,
        related_name='users_backgrnd_color',
        null=True,
        blank=True,
        verbose_name='Цвет бэкграунда',
        help_text='Цвет бэкграунда'
    )


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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['poll', 'question', 'user'],
                name='unique poll try'
            )
        ]


class Purchase(models.Model):
    LOGIN = 'login'
    BACKGROUND = 'backgrnd'
    USER_TYPE_CHOICES = [
        (LOGIN, 'Рамка логина'),
        (BACKGROUND, 'Бэкграунд')
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchases',
        verbose_name='Пользователь',
        help_text='Пользователь'
    )
    color = models.ForeignKey(
        Colors,
        on_delete=models.CASCADE,
        related_name='purchases',
        verbose_name='Цвет',
        help_text='Приобретаемый цвет'
    )
    type = models.CharField(
        max_length=15,
        choices=USER_TYPE_CHOICES,
        verbose_name='Тип',
        help_text='Предмет покупки'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['color', 'user', 'type'],
                name='unique purchase'
            )
        ]
