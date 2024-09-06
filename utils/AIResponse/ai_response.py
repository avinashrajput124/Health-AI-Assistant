from django.conf import settings
from datetime import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

class AIResponseService:
    def __init__(self):
        # Initialize environment variables
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_sleep_response(self, user, sleep_data):
        average_sleep_hours = sum([entry['sleep_time'] / 3600 for entry in sleep_data]) / len(sleep_data)
        if average_sleep_hours < 6:
            advice = "It's important to aim for at least 7-8 hours of sleep each night for better health."
        else:
            advice = "Keep up the good work with your sleep schedule!"

        data = f"User: {user}\nAverage Sleep: {average_sleep_hours:.2f} hours per night\nAdvice: {advice}"
        response = self._get_ai_response(data)
        return response

    def generate_steps_response_1(self, user, step_count):
        data = (f"User: {user}\nSteps Today: {step_count}\n"
                f"Advice: Great job hitting {step_count} steps today! Staying active is crucial for your health.")
        response = self._get_ai_response(data)
        return response

    def generate_steps_response_2(self, user, steps_last_week, steps_previous_week):
        if steps_previous_week > 0:
            percentage_change = ((steps_last_week - steps_previous_week) / steps_previous_week) * 100
        else:
            percentage_change = 0

        change = 'more' if percentage_change < 0 else 'less'
        data = (f"User: {user}\nSteps Last Week: {steps_last_week}\nSteps Previous Week: {steps_previous_week}\n"
                f"Advice: This week, you walked {steps_last_week} steps which is {abs(percentage_change):.2f}% {change} than last week. "
                f"Try to stay consistent with your activity levels to maintain your health and fitness.")
        response = self._get_ai_response(data)
        return response

    def _get_ai_response(self, data):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide concise and personalized health advice based on the provided data. Use a friendly and encouraging tone.dont make it loing."},
                {"role": "user", "content": data}
            ]
        )
        return completion.choices[0].message.content.strip()
