from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.serializers import *


class PageStatView(APIView):
    """
    Save page statistics
    """

    def post(self, request, *args, **kwargs):
        return Response(
            {
                'status': False
            },
            status=status.HTTP_404_NOT_FOUND
        )


class GroupView(APIView):
    """
    Post and get group saving details
    """

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'status': False
            },
            status=status.HTTP_404_NOT_FOUND
        )

    def post(self, request, *args, **kwargs):
        return Response(
            {
                'status': False
            },
            status=status.HTTP_404_NOT_FOUND
        )


class GoalView(APIView):
    """
    Save goal details
    """

    def post(self, request, *args, **kwargs):
        return Response(
            {
                'status': False
            },
            status=status.HTTP_404_NOT_FOUND
        )
