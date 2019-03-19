from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete="models.CASCADE")
    name = models.CharField(max_length=30, blank=True)
    email_id = models.EmailField(
        max_length=70, blank=True, null=True, unique=True)
    # bio = models.TextField(max_length=500, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Task(models.Model):
	Title = models.CharField(max_length=200, blank=True)
	Description = models.TextField(blank=True)
	# comments=models.ManytoManyField(Comments,related_name='comments',on_delete="models.CASCADE")
	Assignee = models.OneToOneField(
		Profile, related_name='profile_name', on_delete="models.CASCADE")
	Status_choices = (
		('P', 'Planned'),
		('IP', 'InProgress'),
		('D', 'Done'),
		)
	Status = models.CharField(max_length=1,choices=Status_choices)

	def __str__(self):
		return self.Title

class Team(models.Model):
	username=models.ManyToManyField(Profile,related_name='usernames')
	team_name=  models.CharField(max_length=200, blank=True)

	def __str__(self):
		self.team_name

class Comments(models.Model):
	username=models.ForeignKey(Profile,related_name='username',on_delete="models.CASCADE")
	task=models.ForeignKey(Task,related_name='task',on_delete="models.CASCADE")
	content=models.TextField(blank=True)
	team=models.ForeignKey(Team,related_name='team',on_delete="models.CASCADE")




























