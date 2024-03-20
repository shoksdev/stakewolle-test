from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Измененная модель пользователя, унаследованная от AbstractUser"""

    referrer_code = models.CharField(max_length=20, null=True, blank=True, verbose_name='Код реферера')

    REQUIRED_FIELDS = ['email', 'referrer_code']


class ReferralCode(models.Model):
    """Модель реферального кода, связана с пользователем полем ОдинКОдному"""

    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, primary_key=True, related_name='referral_code',
                                verbose_name='Пользователь')
    referral_code_title = models.CharField(max_length=20, verbose_name='Реферальный код')
    referral_code_due_date = models.DateTimeField(verbose_name='Срок годности реферального кода')
