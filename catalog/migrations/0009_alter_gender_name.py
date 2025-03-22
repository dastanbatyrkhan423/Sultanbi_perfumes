# Generated by Django 5.1.7 on 2025-03-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_gender_code_alter_gender_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(choices=[('male', 'мужской'), ('female', 'женский'), ('unisex', 'unisex')], default='unisex', max_length=50, verbose_name='Пол'),
        ),
    ]
