# Generated by Django 4.2.7 on 2023-11-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('В ожидании', 'В ожидании'), ('Успешно', 'Успешно'), ('Отмена', 'Отмена')], default='В ожидании', max_length=50),
        ),
    ]
