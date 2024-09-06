from django.core.management.base import BaseCommand
from users.models import AppleHealthStat, UserProfile
import random
from datetime import timedelta, datetime
from django.utils import timezone
import uuid
from utils.Command_helper.help import generate_random_name 

class Command(BaseCommand):
    help = 'Populate the database with random AppleHealthStat data'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        users = []
        # Create 5 random user profiles
        for i in range(5):
            user_id = uuid.uuid4().hex[:8]  
            first_name, last_name = generate_random_name()
            user = UserProfile.objects.create(
                username=f'{user_id}',  # Unique username
                first_name=first_name,
                last_name=last_name,
                email=f'{first_name.lower()}.{user_id}@yopmail.com',  
                password='password123'
            )
            users.append(user)
        
        for user in users:
            # Generate random sleep data for the past 7 days
            sleep_data = [
                {"date": (now - timedelta(days=random.randint(0, 6))).strftime('%Y-%m-%d %H:%M'), 
                 "sleep_time": random.uniform(0.5, 2.0) * 3600} 
                for _ in range(20)  # Create 20 random sleep records
            ]
            AppleHealthStat.objects.create(
                user=user,  # Associate with the user
                dateOfBirth=datetime(1990, 1, 1),  
                height=random.randint(150, 200), 
                bodyMass=random.randint(50, 100),
                bodyFatPercentage=random.randint(10, 30),  
                biologicalSex=random.choice(['male', 'female']), 
                activityMoveMode='activeEnergy', 
                stepCount=random.randint(5000, 15000), 
                basalEnergyBurned=random.randint(800, 1200),
                activeEnergyBurned=random.randint(100, 300),
                flightsClimbed=random.randint(0, 10), 
                appleExerciseTime=random.randint(0, 120), 
                appleMoveTime=random.randint(0, 120),  
                appleStandHour=random.randint(0, 24), 
                menstrualFlow=random.choice(['none', 'light', 'moderate', 'heavy']),  
                HKWorkoutTypeIdentifier=random.choice(['none', 'running', 'cycling', 'swimming']),  
                heartRate=random.randint(50, 100),  
                oxygenSaturation=random.uniform(90, 100),  
                mindfulSession={}, 
                sleepAnalysis=sleep_data  
            )
        
        # Output a success message to the console
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with random data for all users.'))
