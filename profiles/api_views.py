from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Task


class TaskStatusDataView(APIView):
    def get(self, request, user_id=None, format=None) -> Response:

        if user_id is None:
            return Response(
                {"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        tasks = Task.objects.filter(user_id=user_id).values("status")

        status_counts = {
            "in_progress": 0,
            "completed": 0,
        }

        for task in tasks:
            if task["status"]:
                status_counts["completed"] += 1
            else:
                status_counts["in_progress"] += 1

        return Response(status_counts, status=status.HTTP_200_OK)
