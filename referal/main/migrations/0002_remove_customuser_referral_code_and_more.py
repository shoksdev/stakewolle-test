# Generated by Django 5.0.3 on 2024-03-19 10:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='referral_code',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='referral_due_date',
        ),
        migrations.CreateModel(
            name='ReferralCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_code', models.CharField(max_length=20, verbose_name='Код реферера')),
                ('referral_due_date', models.DateTimeField(verbose_name='Срок годности реферального кода')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Пользователь')),
            ],
        ),
    ]
