from django.db import models
from datetime import datetime, timedelta
from django.db.models.deletion import CASCADE


# Create your models here.
# Prescriber name, gender, credentials, location, specialty


class Prescriber(models.Model):
    npi = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.ForeignKey('State', on_delete=CASCADE, db_column= "state")
    credentials = models.CharField(max_length=20)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.CharField(default= 'False', max_length=5)
    totalprescriptions = models.IntegerField(default=0)

    class Meta:
            db_table = "pd_prescriber"

    def __str__(self):
            return (self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.lname, self.fname)

    def save(self):
        self.fname = self.fname.upper()
        self.lname = self.lname.upper()
        super(Prescriber, self).save()


class Drug(models.Model):
    drugid = models.IntegerField(primary_key=True)
    drugname = models.CharField(max_length=30, unique=True)
    isopioid = models.CharField(max_length=5)

    class Meta:
            db_table = "pd_drugs"

    def __str__(self):
        return(self.drugname)

class State(models.Model) :
    state = models.CharField(max_length=14)
    stateabbrev = models.CharField(max_length=2, primary_key=True)
    population = models.IntegerField()
    deaths = models.IntegerField()

    class Meta:
            db_table = "pd_statedata"

    def __str__(self):
        return(self.stateabbrev)


class Triple(models.Model):
    id = models.IntegerField(primary_key=True)
    prescriberid = models.ForeignKey("Prescriber", on_delete=CASCADE, db_column= "prescriberid")
    drugname = models.ForeignKey("Drug", on_delete=CASCADE, to_field = "drugname",  db_column= "drugname")
    qty = models.IntegerField(default=0)

    class Meta:
            db_table = "pd_triple"

class AvgData(models.Model):
        drugname = models.CharField(primary_key =True, max_length=30)
        avgData = models.IntegerField()

class PrescriberOnlyOpioids(models.Model):
        prescriberid = models.IntegerField(primary_key=True)

class highOpioids(models.Model):
        prescriberid = models.IntegerField(primary_key=True)
        pctopioids = models.FloatField()

class OverallPrescriptions(models.Model):
        drugid = models.IntegerField(primary_key=True)
        drugname = models.CharField(max_length=30)
        qtyprescribed = models.IntegerField()




