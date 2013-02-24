from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class NationalUser(models.Model):
    user = models.ForeignKey(UserProfile)
    target_small = models.IntegerField()
    target_big = models.IntegerField()
    target_dewormed = models.IntegerField()

    def __unicode__(self):
        return self.user.name

class RegionalUser(models.Model):
    user = models.ForeignKey(UserProfile)
    national = models.ForeignKey(NationalUser, related_name="regions")
    target_small = models.IntegerField()
    target_big = models.IntegerField()
    target_dewormed = models.IntegerField()

    def __unicode__(self):
        return self.user.name

class DistrictUser(models.Model):
    user = models.ForeignKey(UserProfile)
    regional = models.ForeignKey(RegionalUser, related_name="districts")

    target_small = models.IntegerField()
    target_big = models.IntegerField()
    target_dewormed = models.IntegerField()

    def __unicode__(self):
        return self.user.name

class IndividualUser(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    district = models.ForeignKey(DistrictUser, related_name="individuals")

    def __unicode__(self):
        return self.name

class Report(models.Model):
    date_created = models.DateTimeField()
    owner = models.ForeignKey(IndividualUser, related_name="reports")

    # report info
    supplemented_small = models.IntegerField()
    supplemented_big = models.IntegerField()
    dewormed = models.IntegerField()

    # approval flags
    approved = models.BooleanField(default=False)

    def save(self):
        if self.date_created == None:
            self.date_created = datetime.now()
        super(Report, self).save()

    def __unicode__(self):
        return "Approved? " + str(self.approved) + "; Reported by " + self.owner.__unicode__()
