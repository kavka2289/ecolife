from django.db import migrations

def create_ecohabits(apps, schema_editor):
    EcoHabit = apps.get_model('core', 'EcoHabit')
    habits = [
        {"name": "Сортировка мусора", "description": "Разделяйте отходы на пластик, бумагу, стекло и органику.", "impact_score": 10},
        {"name": "Использование многоразовых сумок", "description": "Откажитесь от пластиковых пакетов в пользу эко-сумок.", "impact_score": 8},
        {"name": "Экономия воды", "description": "Сократите время принятия душа и не оставляйте кран открытым.", "impact_score": 7},
        {"name": "Экономия электроэнергии", "description": "Выключайте свет и электроприборы, когда они не нужны.", "impact_score": 7},
        {"name": "Отказ от одноразовой посуды", "description": "Используйте многоразовую посуду и бутылки.", "impact_score": 9},
        {"name": "Покупка местных продуктов", "description": "Покупайте продукты местного производства для снижения углеродного следа.", "impact_score": 6},
        {"name": "Использование общественного транспорта", "description": "Чаще пользуйтесь общественным транспортом или велосипедом.", "impact_score": 8},
        {"name": "Сбор макулатуры", "description": "Сдавайте бумагу и картон на переработку.", "impact_score": 6},
        {"name": "Посадка деревьев", "description": "Участвуйте в акциях по озеленению города.", "impact_score": 10},
        {"name": "Сокращение потребления пластика", "description": "Откажитесь от лишней упаковки и одноразовых товаров.", "impact_score": 9},
    ]
    for h in habits:
        EcoHabit.objects.create(**h)

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0003_recyclingpoints_moscow_90'),
    ]
    operations = [
        migrations.RunPython(create_ecohabits),
    ] 