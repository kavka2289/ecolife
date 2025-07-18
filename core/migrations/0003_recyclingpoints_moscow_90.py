from django.db import migrations
import random

def create_more_recycling_points(apps, schema_editor):
    RecyclingPoint = apps.get_model('core', 'RecyclingPoint')
    base_lat = 55.75
    base_lon = 37.62
    points = []
    for i in range(11, 101):
        lat = base_lat + random.uniform(-0.08, 0.08)
        lon = base_lon + random.uniform(-0.15, 0.15)
        points.append({
            "name": f"Пункт переработки {i}",
            "address": f"Москва, ул. Примерная, д.{i}",
            "waste_type": "пластик",
            "latitude": round(lat, 6),
            "longitude": round(lon, 6),
        })
    for p in points:
        RecyclingPoint.objects.create(**p)

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_recyclingpoints_moscow'),
    ]
    operations = [
        migrations.RunPython(create_more_recycling_points),
    ] 