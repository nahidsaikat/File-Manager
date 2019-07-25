import pytest
import factory
from faker import Faker
from django.test import Client
from django.urls import reverse

from file_manager.file.tests.factory import FileFactory

fake = Faker()


class BaseFixture:

    @pytest.fixture
    def client(self):
        return Client()


class TestFileView(BaseFixture):

    def test_folder_create(self, client, db):
        data = factory.build(dict, FACTORY_CLASS=FileFactory)
        url = reverse('file:add')
        response = client.post(url, data)
        assert response.status_code == 200

    def test_folder_list(self, client, db):
        FileFactory(name=fake.name().replace(' ', '_'))
        FileFactory(name=fake.name().replace(' ', '_'))
        url = reverse('file:list')
        response = client.get(url)
        assert response.status_code == 200

