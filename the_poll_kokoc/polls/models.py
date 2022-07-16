from django.db import models


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
    OPEN = 'OP'
    SINGLE_ANSWER = 'SA'
    MULTIPLE_ANSWERS = 'MA'
    QUESTION_CHOICES = [
        (OPEN, 'Открытый вопрос'),
        (SINGLE_ANSWER, 'Один ответ'),
        (MULTIPLE_ANSWERS, 'Несколько вариантов ответа'),
    ]
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Опрос',
        help_text='Опрос, в котором находится вопрос'
    )
    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_CHOICES,
        default=SINGLE_ANSWER,
        verbose_name='Тип',
        help_text='Тип вопроса'
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
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст ответа'
    )

    def __str__(self) -> str:
        return self.text
