from django.db import migrations

def create_recycling_points(apps, schema_editor):
    RecyclingPoint = apps.get_model('core', 'RecyclingPoint')
    points = [
        {"name": "Пункт переработки 1", "address": "Москва, ул. Тверская, 1", "waste_type": "пластик", "latitude": 55.757, "longitude": 37.615},
        {"name": "Пункт переработки 2", "address": "Москва, ул. Арбат, 10", "waste_type": "пластик", "latitude": 55.752, "longitude": 37.604},
        {"name": "Пункт переработки 3", "address": "Москва, пр-т Мира, 50", "waste_type": "пластик", "latitude": 55.792, "longitude": 37.636},
        {"name": "Пункт переработки 4", "address": "Москва, ул. Профсоюзная, 20", "waste_type": "пластик", "latitude": 55.677, "longitude": 37.553},
        {"name": "Пункт переработки 5", "address": "Москва, ул. Ленинская Слобода, 26", "waste_type": "пластик", "latitude": 55.708, "longitude": 37.654},
        {"name": "Пункт переработки 6", "address": "Москва, ул. Сущёвский Вал, 5", "waste_type": "пластик", "latitude": 55.792, "longitude": 37.622},
        {"name": "Пункт переработки 7", "address": "Москва, ул. Большая Якиманка, 22", "waste_type": "пластик", "latitude": 55.735, "longitude": 37.609},
        {"name": "Пункт переработки 8", "address": "Москва, ул. Новослободская, 24", "waste_type": "пластик", "latitude": 55.781, "longitude": 37.601},
        {"name": "Пункт переработки 9", "address": "Москва, ул. Маросейка, 7/8", "waste_type": "пластик", "latitude": 55.756, "longitude": 37.634},
        {"name": "Пункт переработки 10", "address": "Москва, ул. Земляной Вал, 33", "waste_type": "пластик", "latitude": 55.755, "longitude": 37.660},
    ]
    for p in points:
        RecyclingPoint.objects.create(**p)

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_recycling_points),
    ] 