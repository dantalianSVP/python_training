from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="One Group", header="MARK", footer="Farenheit"))
    app.session.logout()

# def test_empty_group(app):
#    app.session.login(username="admin", password="secret")
#    app.create_group( Group(name=" ", header=" ", footer=" "))
#    app.session.logout()
