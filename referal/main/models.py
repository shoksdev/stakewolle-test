from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    reference_code = models.CharField(max_length=20, verbose_name='Код реферера')


class ReferralCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, primary_key=True, verbose_name='Пользователь')
    reference_code = models.CharField(max_length=20, verbose_name='Код реферера')
    referral_due_date = models.DateTimeField(verbose_name='Срок годности реферального кода')
