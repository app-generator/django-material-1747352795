# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Nonconformance(models.Model):

    #__Nonconformance_FIELDS__
    identifier = models.TextField(max_length=255, null=True, blank=True)
    date created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date closed = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date modified = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)
    poc = models.CharField(max_length=255, null=True, blank=True)
    program = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    work order = models.CharField(max_length=255, null=True, blank=True)

    #__Nonconformance_FIELDS__END

    class Meta:
        verbose_name        = _("Nonconformance")
        verbose_name_plural = _("Nonconformance")


class Causes(models.Model):

    #__Causes_FIELDS__
    identifier = models.ForeignKey(nonconformance, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, null=True, blank=True)
    poc = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    parent = models.CharField(max_length=255, null=True, blank=True)
    comments = models.TextField(max_length=255, null=True, blank=True)
    id = models.IntegerField(null=True, blank=True)

    #__Causes_FIELDS__END

    class Meta:
        verbose_name        = _("Causes")
        verbose_name_plural = _("Causes")


class Evidence(models.Model):

    #__Evidence_FIELDS__
    id = models.ForeignKey(causes, on_delete=models.CASCADE)
    evidence for = models.TextField(max_length=255, null=True, blank=True)
    evidence against = models.TextField(max_length=255, null=True, blank=True)

    #__Evidence_FIELDS__END

    class Meta:
        verbose_name        = _("Evidence")
        verbose_name_plural = _("Evidence")



#__MODELS__END
