from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Imports for Custom user model
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Other imports
from django_countries.fields import CountryField


# Create your models here.
class CustomUser(AbstractUser):
    """
     Model for custom user with email as the unique identifier.
    """
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        """
        Return the email address as the string representation of the user.
        """
        return self.email

    def get_username(self):
        """
        Return the email address as the string representation of the user.
        """
        return self.username


class UserProfile(models.Model):
    """
    Model for user profile
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    country = CountryField(blank_label='(select country)', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    # home_spot = models.ForeignKey('SurfSpot', on_delete=models.SET_NULL, blank=True, null=True, )
    profile_picture = models.ImageField(upload_to='profile_pictures', default='profile_pictures/def.jpeg')
    # visited_spots = models.ManyToManyField(SurfSpot, blank=True, related_name='visited_spots')
    friends = models.ManyToManyField(CustomUser, blank=True, related_name='friends')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user_profile', args=[str(self.id)])

    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
