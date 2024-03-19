from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    reference_code = models.CharField(max_length=20, verbose_name='Код реферера')


class ReferralCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, primary_key=True, related_name='referral_code',
                                verbose_name='Пользователь')
    referral_code_title = models.CharField(max_length=20, verbose_name='Реферальный код')
    referral_code_due_date = models.DateTimeField(verbose_name='Срок годности реферального кода')
