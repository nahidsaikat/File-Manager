from factory.django import DjangoModelFactory
from faker import Faker

from file_manager.folder.models import Folder

fake = Faker()


class FolderFactory(DjangoModelFactory):
    class Meta:
        model = Folder

    name = fake.name().replace(' ', '_')
    text_color = '#000000'
