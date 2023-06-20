from django.db import models
from django.contrib.auth.models import User
from . import Base, CustomUser, Tag, Section, PostType

class PostBase(Base):
    user = models.ForeignKey(User, on_delete=models.SET(CustomUser.get_deleted_user)) # if User deleted set certain User
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    