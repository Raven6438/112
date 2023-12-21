# Generated by Django 4.1.1 on 2023-12-21 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app112', '0008_alter_appeal_incidents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='status',
            field=models.CharField(choices=[('In_work', 'В работе'), ('Completed', 'Завершено')], default='In_work', max_length=255, verbose_name='Статус'),
        ),
    ]
