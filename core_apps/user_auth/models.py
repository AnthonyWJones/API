import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .emails import send_account_locked_email
from .managers import UserManager

class User(AbstractUser):
    class SecurityQuestion(models.TextChoices):
        MAIDEN_NAME = (
            "maiden_name",
            _("What is your mother's maiden name?"),
        )
        FAVORITE_COLOR=(
            "favorite_color",
            _("What is your favorite color?"),
        )
        BIRTH_CITY = (
            "birth_city", _("What is your birth city?"))
        CHILDHOOD_FRIEND = (
            "childhood_friend",
            _("What is the name of your best chilhood friend?"),
        )

 class AccountStatus(models.TextChoices):
     ACTIVE = "active", _("Active")
     LOCKED = "locked", _("Locked")

 class RoleChoices(models.TextChoices):
     CUSTOMER = "customer", _("Customer")
     ACCOUNT_EXECUTIVE = "account_executive", _("Account Executive")
     TELLER = "teller", _("Teller")
     BRANCH_MANAGER = "branch_manager", _("Branch Manager")

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
username = models.CharField(_("username"), max_length=150, unique=True)







