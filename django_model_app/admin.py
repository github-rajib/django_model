from django.contrib import admin
from django_model_app import models


admin.site.register(models.PostCASCADE)
admin.site.register(models.CommentCASCADE)
admin.site.register(models.PostPROTECT)
admin.site.register(models.CommentPROTECT)
admin.site.register(models.PostSETNULL)
admin.site.register(models.CommentSETNULL)
admin.site.register(models.PostSETDEFAULT)
admin.site.register(models.CommentSETDEFAULT)
admin.site.register(models.PostSET)
admin.site.register(models.CommentSET)
admin.site.register(models.PostDONOTHING)
admin.site.register(models.CommentDONOTHING)
