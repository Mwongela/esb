from django.contrib import admin

# Register your models here.
from django_extensions.db.models import TimeStampedModel, models

from api.models import *


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['phoneNumber', 'deviceBuild']


class PageStatAdmin(admin.ModelAdmin):
    list_display = ['registration', 'timeStamp', 'timeSpent', 'previousPage', 'pageName', 'pageOrder', 'isInputPresent']


class InputStatAdmin(admin.ModelAdmin):
    list_display = ['pageStat', 'name', 'backspaceCount', 'totalKeyPressCount', 'timeStartTyping', 'timeStopTyping',
                    'timeSpentInField', 'finalInputValue', 'finalInputLength', 'intelliWordChanges', 'intelliWordIndex']


class GroupSavingAdmin(admin.ModelAdmin):
    list_display = ['month', 'groupType', 'goalType', 'amount', 'phoneNumber']


class GoalAdmin(admin.ModelAdmin):
    list_display = ['registration', 'groupType', 'goalType', 'goalNote', 'timestamp', 'allowNotifications']


class ContributionAdmin(admin.ModelAdmin):
    list_display = ['goal', 'amount', 'timestamp', 'timestamp', 'contributionVehicle']


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(PageStat, PageStatAdmin)
admin.site.register(InputStat, InputStatAdmin)
admin.site.register(GroupSaving, GroupSavingAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Contribution, ContributionAdmin)
