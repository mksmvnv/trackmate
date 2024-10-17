import logging

from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.users.models import User
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            if not hasattr(instance, "profile"):
                Profile.objects.create(user=instance)
        except Exception as e:
            logger.error(f"Error creating profile for user {instance.id}: {e}")


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        logger.error(f"Profile for user {instance.id} does not exist")
