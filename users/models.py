from django.db import models
from django.utils.translation import ugettext_lazy as _
from tenant_users.tenants.models import UserProfile


# Create your models here.


class TenantUser(UserProfile):
    name = models.CharField(_("Name"), max_length=100, blank=True)
