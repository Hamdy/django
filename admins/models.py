
from django.db import models
from django.utils.translation import gettext_lazy as _

from .fields import UpperCharField
from .managers import PublishedAdminManager

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

class Admin(models.Model):
    name = UpperCharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=user_directory_path)
    is_published = models.BooleanField(default=False)
    
    objects = models.Manager()
    published_objects = PublishedAdminManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print('do something else')

    class Meta:
        verbose_name = _("admin")
        verbose_name_plural = _("admins")
        managed = True # False use existing table
        # db_table = blah
        # abstract : allow inheritance

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=10)
    members = models.ManyToManyField(
        Person,
        through='Membership'
    )
    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )

    date_joined = models.DateTimeField()
