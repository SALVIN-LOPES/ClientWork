from django.db.models.signals import post_save
from django.contrib.auth.models import User
from api.models import Client

# After Registration of User create a client object
def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(
            user=instance,
            name = instance.username,
            )

post_save.connect(create_client,sender=User)