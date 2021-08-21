from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_login, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not user_login:
            raise ValueError('The given user_name must be set')
        user_login = user_login
        user = self.model(user_login=user_login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_login=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_login, password, **extra_fields)

    def create_superuser(self, user_login, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(user_login, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_blogger = models.BooleanField(default=False)
    date_joined = models.DateTimeField('Дата создания', default=timezone.now)
    user_login = models.CharField("Логин", max_length=50, blank=True)
    first_name = models.CharField('Имя', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True)
    followers = models.PositiveIntegerField("Подписчики", default=0)
    event_counter = models.PositiveIntegerField(null=True, default=0)
    email = models.EmailField(unique=False, default="none@gmail.com")

    objects = UserManager()
    USERNAME_FIELD = "user_login"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, verbose_name="Описание мероприятия")
    like = models.PositiveIntegerField(blank=True, null=True, default=0)
    liked_by = models.ManyToManyField(User, null=True, blank=True, related_name="liked")
    comments = models.ManyToManyField("Comment", null=True, blank=True)
    participant = models.ManyToManyField(User, null=True, blank=True, related_name="participants")



    def add_like(self, user_id):
        user = User.objects.get(pk=user_id)
        print(user)
        if user in self.liked_by.all():
            print(1)
            self.update(like=self.like - 1)
            if self.like < 0:
                self.update(like=0)
            self.liked_by.remove(user)
            return
        else:
            self.update(like=self.like + 1)
            self.liked_by.add(user)
            return
        """if user in obj.liked_by.all():
            obj.liked_by.remove(user)
            print("removed")
        else:
            obj.liked_by.add(user)
            print("success")"""

class Comment(models.Model):
    message = models.CharField(max_length=255, verbose_name="Текст комментария")

    def __str__(self):
        return self.message
