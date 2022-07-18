from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Colors, User, Poll, Question, Answer, UserAnswer


admin.site.register(User, UserAdmin)
admin.site.register(Colors)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserAnswer)
