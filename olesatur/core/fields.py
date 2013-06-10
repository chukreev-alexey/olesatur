# -*- coding: utf-8 -*-
import re

from django.db import models
from django.core.validators import validate_email

from south.modelsinspector import add_introspection_rules

def emails_list(value):
    return filter(lambda x: bool(x.strip()), re.split(r'[,|;]?\s?', value or ''))

class MultiEmailField(models.CharField):
    def validate(self, value, model_instance):
        super(MultiEmailField, self).validate(value, model_instance)
        for email in emails_list(value):
            validate_email(email)

add_introspection_rules([], ["^common\.fields\.MultiEmailField"])
