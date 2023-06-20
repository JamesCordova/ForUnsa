from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from . import Base, Status, School

class CustomUser(User, Base):
    # id, name, last_name, email, nickname, is_admin, is_staff included on User
    current_school = models.ForeignKey(School, on_delete=models.SET(School.get_default_school)) # School of the user e.g. System Engineering
    biography = models.CharField(max_length=255, blank=True) # description of user
    img = models.ImageField(upload_to='profiles', default='default.jpg')
    is_featured = models.BooleanField(default=False) # user is featured
    semester = models.CharField(max_length=32, default='not defined') # inital semester
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=Status.get_default_status) # Grade status
    slug = models.SlugField(max_length=64, unique=True, editable=False) # slug for links
    
    def get_deleted_user():
        return CustomUser.objects.get_or_create(username="Deleted", )[0]
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)