import pytest
from faker import Faker

from file_manager.folder.models import Folder
from file_manager.folder.tests.factory import FolderFactory

fake = Faker()


class TestFolder:

    @pytest.mark.django_db
    def test_folder_create(self):
        FolderFactory(name=fake.name())
        FolderFactory(name=fake.name())

        assert Folder.objects.count() == 2
