# Generated by Django 4.2.7 on 2024-01-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_confirm_code_alter_user_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.CharField(default='300996', max_length=6, verbose_name='Код'),
        ),
    ]
