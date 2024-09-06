# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class UserProfile(AbstractUser):
    email = models.EmailField(unique=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=16, null=True)
    country_code = models.CharField(max_length=5, default='+91')
    address = models.TextField(null=True, blank=True)
    password_changed_at = models.DateTimeField(auto_now=True)
    user_invalid_attempt = models.IntegerField(default=0)
    user_invalid_attempt_at = models.DateTimeField(
        null=True,
        blank=False)
    user_timezone = models.CharField(
        max_length=250, null=True, blank=True, default="Asia/Kolkata")
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email

class AppleHealthStat(models.Model):
    """
    Model for storing Apple Health data for users.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='apple_health_stat')
    dateOfBirth = models.DateTimeField(null=True, blank=True)
    height = models.PositiveSmallIntegerField(null=True, blank=True)
    bodyMass = models.PositiveSmallIntegerField(null=True, blank=True) # Height in cm
    bodyFatPercentage = models.PositiveSmallIntegerField(null=True, blank=True)
    biologicalSex = models.CharField(max_length=32, null=True, blank=True)
    activityMoveMode = models.CharField(max_length=128, null=True, blank=True)
    stepCount = models.PositiveSmallIntegerField(null=True, blank=True) # Daily step count
    basalEnergyBurned = models.PositiveSmallIntegerField(null=True, blank=True)
    activeEnergyBurned = models.PositiveSmallIntegerField(null=True, blank=True)
    flightsClimbed = models.PositiveSmallIntegerField(null=True, blank=True)
    appleExerciseTime = models.PositiveSmallIntegerField(null=True, blank=True)
    appleMoveTime = models.PositiveSmallIntegerField(null=True, blank=True)
    appleStandHour = models.PositiveSmallIntegerField(null=True, blank=True)
    menstrualFlow = models.CharField(max_length=128, null=True, blank=True)
    HKWorkoutTypeIdentifier = models.CharField(max_length=128, null=True, blank=True)
    heartRate = models.PositiveSmallIntegerField(null=True, blank=True) # Average heart rate
    oxygenSaturation = models.PositiveSmallIntegerField(null=True, blank=True) # Sleep analysis in JSON format (list of dicts with date and sleep_time)
    mindfulSession = models.JSONField(null=True, blank=True)
    sleepAnalysis = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.date()}"
