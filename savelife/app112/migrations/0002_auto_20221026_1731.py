# Generated by Django 4.1.2 on 2022-10-26 12:31

from django.db import migrations, transaction


def add_service(apps, schema_editor):
    service = apps.get_model('app112', 'EmergencyService')
    with transaction.atomic():
        service.objects.create(title='Полиция')
        service.objects.create(title='Скорая помощь')
        service.objects.create(title='Пожарная служба')

class Migration(migrations.Migration):

    dependencies = [
        ('app112', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_service)
    ]
