from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **kwargs):
        '''
        创建用户
        '''
        if not email:
            raise ValueError("Users must have avalid email!!")
        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, username, email, password, **kwargs):
        """
        创建超级管理用户
        """
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
