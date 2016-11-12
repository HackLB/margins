from django.contrib import admin
import core.models

admin.site.register(core.models.Body)
admin.site.register(core.models.Document)
admin.site.register(core.models.Meeting)