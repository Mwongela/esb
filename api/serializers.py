from rest_framework import serializers

from api.models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class PageStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageStat
        fields = '__all__'


class InputStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputStat
        fields = '__all__'


class GroupSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSaving
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'
