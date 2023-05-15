from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    time_taken = models.DurationField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clue_1_completed = models.BooleanField(default=False)
    clue_1_time = models.DurationField(null=True, blank=True)
    clue_2_completed = models.BooleanField(default=False)
    clue_2_time = models.DurationField(null=True, blank=True)
    clue_3_completed = models.BooleanField(default=False)
    clue_3_time = models.DurationField(null=True, blank=True)
    clue_4_completed = models.BooleanField(default=False)
    clue_4_time = models.DurationField(null=True, blank=True)
    clue_5_completed = models.BooleanField(default=False)
    clue_5_time = models.DurationField(null=True, blank=True)
    deadend_1_time=models.DurationField(null=True, blank=True)
    deadend_2_time=models.DurationField(null=True, blank=True)