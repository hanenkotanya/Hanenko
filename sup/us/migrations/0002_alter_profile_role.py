# Generated by Django 4.2.5 on 2023-09-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('None', 'Обозначьте статус задачи'), ('Пользователь', 'Пользователь'), ('Соппорт', 'Соппорт')], default='b', max_length=50, null=True, verbose_name='Роль'),
        ),
    ]
