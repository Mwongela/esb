import uuid

import django
from django_extensions.db.models import TimeStampedModel, models


class Registration(TimeStampedModel):
    phoneNumber = models.CharField(max_length=256)
    deviceBuild = models.CharField(max_length=256)
    lastSeen = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = (("phoneNumber", "deviceBuild"),)

    def __str__(self):
        return "{}-{}".format(self.phoneNumber, self.deviceBuild)


class PageStat(TimeStampedModel):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    timeStamp = models.BigIntegerField(null=False, blank=False)
    timeSpent = models.BigIntegerField(null=False, blank=False)
    previousPage = models.CharField(max_length=256)
    pageName = models.CharField(max_length=256)
    pageOrder = models.IntegerField()
    isInputPresent = models.BooleanField(default=False)

    def __str__(self):
        return self.pageName


class InputStat(TimeStampedModel):
    pageStat = models.ForeignKey(PageStat, on_delete=models.CASCADE)
    backspaceCount = models.IntegerField(default=0)
    totalKeyPressCount = models.IntegerField(default=0)
    timeStartTyping = models.BigIntegerField(default=0)
    timeStopTyping = models.BigIntegerField(default=0)
    timeSpentInField = models.BigIntegerField(default=0)
    finalInputValue = models.CharField(max_length=256)
    finalInputLength = models.IntegerField(default=0)
    intelliWordChanges = models.TextField(blank=True, null=True)
    intelliWordIndex = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class GroupSaving(TimeStampedModel):
    secondaryId = models.UUIDField(unique=True, max_length=256)
    month = models.CharField(max_length=256)
    groupType = models.CharField(max_length=256)
    goalType = models.CharField(max_length=256)
    amount = models.FloatField(default=0)
    phoneNumber = models.CharField(max_length=256)

    def __str__(self):
        return "{}-{}-{}".format(self.phoneNumber, self.month, self.amount)


class Goal(TimeStampedModel):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    groupType = models.CharField(max_length=256)
    goalType = models.CharField(max_length=256)
    goalNote = models.CharField(max_length=256)
    timestamp = models.BigIntegerField(default=0)
    allowNotifications = models.BooleanField(default=True)

    def __str__(self):
        return "{}-{}".format(self.goalType, self.groupType)


class Contribution(TimeStampedModel):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    timestamp = models.BigIntegerField()
    contributionVehicle = models.TextField()
