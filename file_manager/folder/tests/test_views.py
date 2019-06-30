import pytest
import factory
from faker import Faker
from django.test import Client
from django.urls import reverse

from file_manager.folder.models import Folder
from file_manager.folder.tests.factory import FolderFactory

fake = Faker()


class BaseFixture:

    @pytest.fixture
    def client(self):
        return Client()


class TestFolderView(BaseFixture):

    def test_folder_create(self, client, db):
        data = factory.build(dict, FACTORY_CLASS=FolderFactory)
        url = reverse('folder:add')
        response = client.post(url, data)
        assert response.status_code == 302

    def test_folder_list(self, client, db):
        FolderFactory(name=fake.name().replace(' ', '_'))
        FolderFactory(name=fake.name().replace(' ', '_'))
        url = reverse('folder:list')
        response = client.get(url)
        assert response.status_code == 200

