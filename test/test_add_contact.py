# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.application import Application
import pytest
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_page_for_create_contact()
    app.contact.fill_from(Contact(firstname="Slaughter", middlename="To", lastname="Preval", nickname="Dln",
                                  title="RRR", company="TANDER", address="SORMOVSKAYA", home="serious", mobile="123456",
                                  work="123456", fax="123456", email="spektakl_okon4en@mail.ru", email2="asdasd",
                                  email3="asdasd", homepage="asdasdasd"))
    app.contact.fill_bday()
    app.contact.fill_aday()
    app.contact.submit()
    app.contact.return_to_home_page()
    app.session.logout()
