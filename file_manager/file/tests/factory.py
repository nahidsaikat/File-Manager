import factory
from faker import Faker
from factory.django import DjangoModelFactory
from django.conf import settings

from file_manager.folder.tests.factory import FolderFactory
from file_manager.file.models import File

fake = Faker()


class FileFactory(DjangoModelFactory):
    class Meta:
        model = File

    name = fake.name().replace(' ', '_')
    folder = factory.SubFactory(FolderFactory)
    path = str(settings.BASE_DIR)
