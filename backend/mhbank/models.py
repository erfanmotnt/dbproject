from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Account(models.Model):
    username = models.CharField(max_length=40, primary_key=True)
    firstname = models.CharField(max_length=30, default='None')
    lastname = models.CharField(max_length=30, default='None')
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    role = models.CharField(max_length=1)
    srate = models.IntegerField(default=0)
    crate = models.IntegerField(default=0)


class Tag(models.Model):
    tname = models.CharField(max_length=200, primary_key = True)
    cusername = models.ForeignKey("Account", null = True, on_delete=models.SET_NULL)

    # sub_tags
    def __str__(self):
        return self.tname


class SubTag(models.Model):
    tname = models.ForeignKey("Tag", on_delete=models.CASCADE)
    stname = models.CharField(max_length=200)
    cusername = models.ForeignKey("Account", null = True, on_delete=models.SET_NULL, related_name="subtags")
    dusername = models.ForeignKey("Account", null = True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

    class Meta:
        unique_together = (("tname", "stname"),)


class Event(models.Model):
    ename = models.CharField(max_length=200, primary_key=True)
    cusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL)
    cdate = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name


class Problem(models.Model):
    pid = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=1)
    score = models.IntegerField(default=0)
    text = models.TextField()
    
    cusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL, related_name="cproblems")
    cdate = models.DateTimeField(null=True)
    chusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL, related_name="chproblems")
    chdate = models.DateTimeField(null=True)
    dusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL, related_name="dproblems")
    ddate = models.DateTimeField(null=True)
    
    level = models.IntegerField(default=5)
    minaar = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    maxaar = models.IntegerField(
        default=12,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    vusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL)
    vcomment = models.CharField(max_length=1000, null=True)
    rsid = models.ForeignKey("Resource", null=True, on_delete=models.SET_NULL)

class PRU(models.Model):
    pid = models.ForeignKey("Problem", on_delete=models.CASCADE)
    username = models.ForeignKey("Account", on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    class Meta:
        unique_together = (("pid", "username"),)

class Answer(models.Model):
    pid = models.ForeignKey("Problem", on_delete=models.CASCADE)
    anum = models.IntegerField()
    text = models.TextField()
    cusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL, related_name="answers")
    cdate = models.DateTimeField(null=True)
    chusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL)
    chdate = models.DateTimeField(null=True)
    class Meta:
        unique_together = (("pid", "anum"),)


class Guidance(models.Model):
    pid = models.ForeignKey("Problem", on_delete=models.CASCADE)
    gnum = models.IntegerField()
    anum = models.ForeignKey("Answer", on_delete=models.CASCADE)
    text = models.TextField()
    cusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL, related_name="guidances")
    cdate = models.DateTimeField(null=True)
    chusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL)
    chdate = models.DateTimeField(null=True)
    class Meta:
        unique_together = (("pid", "gnum"),)

class Resource(models.Model):
    rsid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL, related_name="resources")
    cdate = models.DateTimeField(null=True)
    chusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL)
    chdate = models.DateTimeField(null=True)


class TeachBox(models.Model):
    pid = models.ForeignKey("Problem", on_delete=models.CASCADE)
    answer = models.ForeignKey("Answer", on_delete=models.CASCADE)
    explanation = models.TextField(null=True)
    goal = models.TextField(null=True)
    time = models.TimeField(null=True)
    
    cusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL, related_name="teachboxes")
    cdate = models.DateTimeField(null=True)
    chusername = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL)
    chdate = models.DateTimeField(null=True)
    
    class Meta:
        unique_together = (("pid", "answer"),)

