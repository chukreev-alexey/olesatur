# -*- coding: utf-8 -*-
from django.db import models

class VisibleObjectsManager(models.Manager):
    def get_query_set(self):
        return super(VisibleObjectsManager, self).get_query_set().filter(visible=True)