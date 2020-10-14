from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MediaStorage(S3Boto3Storage):
    location = settings.AWS_MEDIAFILES_LOCATION
    file_overwrite = False

class StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATICFILES_LOCATION
    file_overwrite = False