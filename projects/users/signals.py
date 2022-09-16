from django.db.models.signals import post_save, post_delete

from .models import Profile, User


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.name,
            email=user.email,
            name=user.first_name
        )


post_save.connect(create_profile, sender=User)


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_delete.connect(delete_user, sender=Profile)
