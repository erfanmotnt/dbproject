from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, unique=True, related_name='account')
    first_name = models.CharField(max_length=30, default='None')
    last_name = models.CharField(max_length=30, default='None')
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    # added_questions
    # attempts
    scientific_rate = models.IntegerField(default=0)
    contribution_rate = models.IntegerField(default=0)
    role = models.CharField(max_length=1)

    # image_url ... not complete

    def __str__(self):
        return self.user.username

    def numberOfAdds(self):
        self.contribution_rate = len(self.question_set.all())
        self.save()
        return len(self.question_set.all())

    def is_adder(self):
        return self.role == 'a'

    def is_mentor(self):
        return self.role == 'm'

    def is_superuser(self):
        return self.role == 's'


class Source(models.Model):
    name = models.CharField(max_length=200)

    # questions



class Tag(models.Model):
    tname = models.CharField(max_length=200, primary_key = True)
    cusername = models.ForeignKey(Account, null = True, on_delete=models.SET_NULL)

    # sub_tags
    def __str__(self):
        return self.tname


class Sub_tag(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)

    # questions

    def __str__(self):
        return self.name


class Problem(models.Model):
    pid = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=200)
    verification_status = models.CharField(max_length=50)
    verification_comment = models.CharField(max_length=1000, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    sub_tags = models.ManyToManyField(Sub_tag, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    source = models.ForeignKey(Source, blank=True, null=True, on_delete=models.SET_NULL)
    question_maker = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    # answer = models.CharField(max_length=3000, null=True, blank=True)
    # guidance = models.CharField(max_length=1000)
    publish_date = models.DateTimeField('date published')
    change_date = models.DateTimeField(null=True, blank=True)
    #hardness
    # themed_qs
    # emoj

    def __str__(self):
        return self.name


class Answer(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True, related_name='answers')
    text = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    change_date = models.DateTimeField(null=True, blank=True)
    publish_date = models.DateTimeField('date published', null=True, blank=True)

    # guidances
    # comments
    # is it original?(not student writen)
    # likes
    # teaches

class Guidance(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    text = models.TextField()
    change_date = models.DateTimeField(null=True, blank=True)
    publish_date = models.DateTimeField('date published', null=True, blank=True)


class Teach_box(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    goal = models.CharField(max_length=1000, null=True, blank=True)
    expectations = models.CharField(max_length=1000, null=True, blank=True)
    # notes
    time = models.TimeField(null=True)
    generalـprocess = models.CharField(max_length=3000)
    change_date = models.DateTimeField(null=True, blank=True)
    publish_date = models.DateTimeField('date published', null=True, blank=True)

