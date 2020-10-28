from abc import ABC

from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MediaStorage(S3Boto3Storage):

    def get_accessed_time(self, name):
        pass

    def get_created_time(self, name):
        pass

    def path(self, name):
        pass

    location = settings.AWS_MEDIAFILES_LOCATION
    file_overwrite = False


class StaticStorage(S3Boto3Storage):
    def path(self, name):
        pass

    def get_accessed_time(self, name):
        pass

    def get_created_time(self, name):
        pass

    location = settings.AWS_STATICFILES_LOCATION
    file_overwrite = False
