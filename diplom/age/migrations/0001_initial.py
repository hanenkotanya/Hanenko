# Generated by Django 4.2.7 on 2023-11-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(choices=[('choises', 'choises'), ('1_4', 'Animators for 1-4 years'), ('5_9', 'Animators for 5-9 years'), ('10_14', 'Animators for 10-14 years')], default='choises', max_length=50)),
            ],
        ),
    ]
