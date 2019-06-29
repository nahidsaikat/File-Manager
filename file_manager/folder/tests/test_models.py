import pytest
from faker import Faker

from file_manager.folder.models import Folder
from file_manager.folder.tests.factory import FolderFactory

fake = Faker()


class BaseFixture:

    @pytest.fixture
    def folder_1(self, db):
        return FolderFactory(name=fake.name().replace(' ', '_'))

    @pytest.fixture
    def folder_2(self, db):
        return FolderFactory(name=fake.name().replace(' ', '_'))


class TestFolder(BaseFixture):

    def test_folder_create(self, folder_1, folder_2):
        assert Folder.objects.count() == 2

    def test_folder_str(self, folder_1, folder_2):
        folder_2.parent = folder_1
        folder_2.save()

        assert str(folder_2) == f'{folder_1.name}::{folder_2.name}'

    def test_folder_depth(self, folder_1, folder_2):
        folder_2.parent = folder_1
        folder_2.save()

        assert folder_2.depth == 1

    def test_parent_url(self, folder_1, folder_2):
        folder_2.parent = folder_1
        folder_2.save()

        assert folder_2.parent_url() == ['/?id=1']
