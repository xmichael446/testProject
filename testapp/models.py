from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DataType(TimestampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Record(TimestampedModel):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE)
    recorded_date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        ordering = ['-recorded_date']


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
