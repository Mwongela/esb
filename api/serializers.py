from rest_framework import serializers

from api.models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration


class PageStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageStat


class InputStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputStat


class GroupSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSaving


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
