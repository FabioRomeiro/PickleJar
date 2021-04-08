from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.CASCADE)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Credential(models.Model):
    class Status(models.TextChoices):
        STRONG = 'strong'
        MEDIUM = 'medium'
        UNSAFE = 'unsafe'
        OBVIOUS = 'obvius'

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image = models.CharField(null=True, blank=True, max_length=500)
    link = models.CharField(null=True, blank=True, max_length=255)
    notes = models.TextField(null=True, blank=True)
    favorite = models.BooleanField(default=False)
    status = models.CharField(null=True, blank=True, max_length=15, choices=Status.choices)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    last_updated = models.DateTimeField('atualizado em', auto_now=True)
    last_accessed = models.DateTimeField('acessado em', auto_now=True)

    def to_dict_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'image': self.image,
            'link': self.link,
            'notes': self.notes,
            'favorite': self.favorite,
            'status': self.status,
            'created_at': self.created_at,
            'last_updated': self.last_updated,
            'last_accessed': self.last_accessed
        }
