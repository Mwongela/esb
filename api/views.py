import datetime

from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.serializers import *


class PageStatView(APIView):
    """
    Save page statistics
    """

    def post(self, request, *args, **kwargs):

        data = request.data
        errors = []
        if data is None:
            return Response(
                {
                    "status": False
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        deviceBuild = data.get('deviceBuild', None)
        phoneNumber = data.get("phoneNumber", None)

        if phoneNumber is None:
            return Response({status: False}, status=status.HTTP_400_BAD_REQUEST)

        registration, created = Registration.objects.get_or_create(deviceBuild=deviceBuild, phoneNumber=phoneNumber)
        pageStats = data.get("pageStats", None)

        registration.lastSeen = datetime.datetime.now()
        registration.save()

        if pageStats:
            for pageStat in pageStats:
                pageStat["registration"] = registration.id
                pageStatSerializer = PageStatSerializer(data=pageStat)
                if pageStatSerializer.is_valid():
                    pageStatObj = pageStatSerializer.save()

                    if pageStat.get("isInputPresent", "no") == "yes":
                        inputStat = pageStat.get("inputStats", None)
                        if inputStat:
                            inputStat["pageStat"] = pageStatObj.id
                            inputStatSerializer = InputStatSerializer(data=inputStat)
                            if inputStatSerializer.is_valid():
                                inputStatSerializer.save()
                            else:
                                errors.append(inputStatSerializer.errors)
                else:
                    errors.append(pageStatSerializer.errors)

        if len(errors) > 0:
            return Response(
                {
                    "status": False,
                    "errors": errors
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        else:
            return Response(
                {
                    "status": True
                },
                status=status.HTTP_200_OK
            )

class GroupView(APIView):
    """
    Post and get group saving details
    """
    def post(self, request, *args, **kwargs):

        try:
            data = request.data
            groupSavings = data.get("groupSaving", None)
            recordsInMyPossession = data.get("recordsInMyPossession", None)
            syncGoalGroups = data.get("groups", None)

            for gs in groupSavings:
                GroupSaving.objects.update_or_create(**gs)

            queryset = GroupSaving.objects.exclude(secondaryId__in=recordsInMyPossession)
            # if syncGoalGroups:
            #     for x in syncGoalGroups:
            #         y = x.split(",")
            #         queryset = queryset | queryset.filter(Q(groupType=y[0]) & Q(goalType=y[1]))

            serializer = GroupSavingSerializer(queryset, many=True)

            return Response(
                {
                    'status': True,
                    'newRecords': serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "status": False
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GoalView(APIView):
    """
    Save goal details
    """

    def post(self, request, *args, **kwargs):
        errors = []
        data = request.data
        if not data:
            return Response(
                {
                    'status': False
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        deviceBuild = data.get('deviceBuild', None)
        phoneNumber = data.get("phoneNumber", None)

        if phoneNumber is None:
            return Response({status: False}, status=status.HTTP_400_BAD_REQUEST)

        registration, created = Registration.objects.get_or_create(deviceBuild=deviceBuild, phoneNumber=phoneNumber)
        registration.lastSeen = datetime.datetime.now()
        registration.save()

        goals = data.get("goals", None)
        if goals:
            for goal in goals:
                goal["registration"] = registration.id
                goalSerializer = GoalSerializer(data=goal)
                if (goalSerializer.is_valid()):
                    goalObj = None
                    if goal["uploaded"]:
                        goalObj = Goal.objects.get(timestamp=goal["timestamp"])
                    else:
                        goalObj = goalSerializer.save()

                    contributions = goal.get("contributions", None)
                    if contributions:
                        for contribution in contributions:
                            contribution["goal"] = goalObj.id
                            contributionSerializer = ContributionSerializer(data=contribution)
                            if contributionSerializer.is_valid():
                                contributionSerializer.save()
                            else:
                                errors.append(contributionSerializer.errors)


                else:
                    errors.append(goalSerializer.errors)

        if len(errors) > 0:
            return Response(
                {
                    "status": False,
                    "errors": errors
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        else:
            return Response(
                {
                    "status": True
                },
                status=status.HTTP_200_OK
            )
