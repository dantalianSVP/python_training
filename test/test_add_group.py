
from model.group import Group
from fixture.application import  Application
import pytest

@pytest.fixture()
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(self):
    self.app.login(username="admin", password="secret")
    self.app.create_group( Group(name="One Group", header="MARK", footer="Farenheit"))
    self.app.logout()

def test_empty_group(self):
    self.app.login(username="admin", password="secret")
    self.app.create_group( Group(name=" ", header=" ", footer=" "))
    self.app.logout()

