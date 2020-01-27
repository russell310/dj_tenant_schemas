from django.db import models
from tenant_users.compat import TENANT_SCHEMAS
from tenant_users.tenants.models import TenantBase


# Create your models here.


class Client(TenantBase):
    auto_drop_schema = True
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
