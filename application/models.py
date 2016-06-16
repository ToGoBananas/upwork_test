from __future__ import unicode_literals

from model_utils.models import TimeStampedModel
from django.contrib.postgres.fields import JSONField


class SampleA(TimeStampedModel):
    purchases = JSONField()

    def __unicode__(self):
        return str(self.created)


class SampleB(TimeStampedModel):
    savings = JSONField()

    def __unicode__(self):
        return str(self.created)
