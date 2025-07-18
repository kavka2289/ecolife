
from django.db import models
from django.contrib.auth.models import User

class EcoHabit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    impact_score = models.FloatField()  # оценка пользы для экологии

class RecyclingPoint(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    waste_type = models.CharField(max_length=100)  # пластик, стекло и т.д.
    latitude = models.FloatField()
    longitude = models.FloatField()

class UserHabit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.ForeignKey(EcoHabit, on_delete=models.CASCADE)
    date_started = models.DateField()

class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class MLModelResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eco_score = models.FloatField()
    prediction_date = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
