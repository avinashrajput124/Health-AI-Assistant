from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import AppleHealthStat
from utils.AIResponse.ai_response import AIResponseService

class SleepConditionAPI(APIView):
    """
    API view for retrieving sleep condition data.
    """
    permission_classes = [AllowAny] 

    def get(self, request):
        """
        Handle GET requests to retrieve sleep condition data.
        """
        # Query for AppleHealthStat objects with non-null sleep analysis data
        users = AppleHealthStat.objects.filter(sleepAnalysis__isnull=False)
        ai_service = AIResponseService()
        response_data = []

        # Process each user's health stats
        for health_stat in users:
            user = health_stat.user.first_name + ' ' + health_stat.user.last_name
            sleep_data = health_stat.sleepAnalysis
            ai_response = ai_service.generate_sleep_response(user, sleep_data)
            response_data.append({
                "user": health_stat.user.username,
                "ai_response": ai_response
            })
        return Response(response_data, status=200)


class StepCondition1API(APIView):
    """
    API view for retrieving step condition data (Condition 1).
    """
    permission_classes = [AllowAny] 

    def get(self, request):
        """
        Handle GET requests to retrieve step condition data (Condition 1).
        """
        users = AppleHealthStat.objects.filter(stepCount__isnull=False)
        ai_service = AIResponseService()
        response_data = []
        # Process each user's health stats
        for health_stat in users:
            user = health_stat.user.first_name + ' ' + health_stat.user.last_name
            step_count = health_stat.stepCount
            ai_response = ai_service.generate_steps_response_1(user, step_count)
            response_data.append({
                "user": user,
                "ai_response": ai_response
            })
        return Response(response_data, status=200)


class StepCondition2API(APIView):
    """
    API view for retrieving step condition data (Condition 2).
    """
    permission_classes = [AllowAny]  

    def get(self, request):
        """
        Handle GET requests to retrieve step condition data (Condition 2).
        """
        # Query for AppleHealthStat objects with non-null step count data
        users = AppleHealthStat.objects.filter(stepCount__isnull=False)
        ai_service = AIResponseService()
        response_data = []
        # Process each user's health stats
        for health_stat in users:
            user = health_stat.user.first_name + ' ' + health_stat.user.last_name
            steps_last_week = health_stat.stepCount
            steps_previous_week = health_stat.stepCount - 500  
            ai_response = ai_service.generate_steps_response_2(user, steps_last_week, steps_previous_week)
            response_data.append({
                "user": user,
                "ai_response": ai_response
            })
        return Response(response_data, status=200)
