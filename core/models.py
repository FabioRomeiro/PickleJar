from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    objects = UserManager()

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    passcoord = models.BinaryField(null=False, blank=False)
    passimage_url = models.CharField(default='', max_length=300)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    credential = models.ForeignKey('core.Credential', null=True, blank=True, on_delete=models.CASCADE)
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
    image = models.CharField(blank=True, max_length=500, default='')
    link = models.CharField(blank=True, max_length=255, default='')
    notes = models.TextField(blank=True, default='')
    favorite = models.BooleanField(default=False)
    status = models.CharField(blank=True, max_length=15, choices=Status.choices, default=Status.OBVIOUS)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    last_updated = models.DateTimeField('atualizado em', auto_now=True)
    last_accessed = models.DateTimeField('acessado em', auto_now=True)

    def __str__(self):
        if self.link:
            return f'{self.name} - {self.link}'
        return self.name

    def to_dict_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'image': self.image,
            'link': self.link,
            'notes': self.notes,
            'favorite': self.favorite,
            'status': str(self.status),
            'created_at': str(self.created_at),
            'last_updated': str(self.last_updated),
            'last_accessed': str(self.last_accessed)
        }

    __dictjson__ = to_dict_json
