from django.db import models

# Create your models here.
from ls.joyous.models import (MultidayEventPage, RecurringEventPage,
                              MultidayRecurringEventPage, removeContentPanels)

# Hide unwanted event types
MultidayEventPage.is_creatable = True
RecurringEventPage.is_creatable = True
MultidayRecurringEventPage.is_creatable = True

# Hide unwanted content
removeContentPanels(["category", "tz", "group_page", "website"])