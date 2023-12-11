from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, nickname, email, password, **extra_fields):
        if not email:
            raise ValueError('Email을 입력해주세요.')
        email = self.normalize_email(email)
        nickname = self.model.normalize_username(nickname)
        user = self.model(nickname=nickname, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self, nickname, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, nickname, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=True일 필요가 있습니다.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=True일 필요가 있습니다.')
        return self._create_user(nickname, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    nickname = models.CharField(_("닉네임"), max_length=50, validators=[username_validator], blank=True)
    email = models.EmailField(_("이메일"), unique=True)
    profile = models.ImageField(_("프로필 사진"), upload_to='profile/',null=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)