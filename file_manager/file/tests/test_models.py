import pytest
from faker import Faker

from file_manager.file.models import File
from file_manager.file.tests.factory import FileFactory

fake = Faker()


class BaseFactory:

    @pytest.fixture
    def file_1(self, db):
        return FileFactory(name=fake.name().replace(' ', '_')+'.txt')

    @pytest.fixture
    def file_2(self, db):
        return FileFactory(name=fake.name().replace(' ', '_')+'.pdf')


class TestFile(BaseFactory):

    def test_create_file(self, file_1, file_2):
        assert File.objects.count() == 2

    def test_full_path(self, file_1):
        assert file_1.full_path == f'{str(file_1.folder)}::{file_1.name}'

    def test_extension(self, file_2):
        assert file_2.extension == file_2.name.split('.')[-1]
