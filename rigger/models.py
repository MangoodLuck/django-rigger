from django.db import models
from datetime import datetime
from rigger.utils import timestamp


class CommonDateModel(models.Model):
    """
    a common model class:
    offer logical delete field is_delete
    """
    created_at = models.DateTimeField(db_index=True,
                                      auto_now_add=True,
                                      verbose_name='createtime',
                                      help_text="createtime")

    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='updatetime',
                                      help_text="updatetime")

    created_user = models.CharField(max_length=128,
                                    null=True,
                                    blank=True,
                                    verbose_name='createuser',
                                    help_text="createuser")

    is_delete = models.FloatField(default=0, help_text="if delete，save float timestamp is deleted")

    class Meta:
        abstract = True

    def created(self):
        return str(datetime.strftime(self.created_at, "%Y-%m-%d %H:%M:%S"))

    def updated(self):
        return str(datetime.strftime(self.updated_at, "%Y-%m-%d %H:%M:%S"))

    def logical_delete(self):
        self.is_delete = timestamp()
        self.save()
