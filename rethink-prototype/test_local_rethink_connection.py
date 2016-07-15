# These are the functional tests for the database connection

import rethinkdb as r
import pytest


    # The app gets a request to call something from the database
    # so it requests a connection.
@pytest.fixture
def conn():
    conn = r.connect('localhost',32796).repl()
    return conn


DATABASE = 'aggregator'
TABLE = 'default'


    # Once the connection is established the app would like to
    # call the correct database.
def test_app_connects_to_correct_db(conn):

    databases = r.db_list().run()

    assert DATABASE in databases


    # Once it has the correct database it would like to use the
    # right table.
def test_app_uses_correct_table(conn):
    tables = r.db(DATABASE).table_list().run()

    assert TABLE in tables


    # Now it is time to insert something into the table.
def test_app_can_add_something_to_table(conn):
    item = [{
        'name':'General Troll',
        'vehicle':'Comments section on the internet',
        'targets': [
            {'type':'human','title':'candidate','name':'Hillary Clinton'},
            {'type':'hobit','title':'ring-bearer','name':'Frodo Baggins'},
            {'type':'human','title':'candidate','name':'Donald Trump'},
            {'type':'omicronian','title':'Ruler of Omicron Persei 8','name':'Lrrr'}
            ] }]
    response = r.db(DATABASE).table(TABLE).insert(item).run()

    assert response['inserted'] == 1


    # Since this is only a test let's go ahead delete that entry.
def test_app_can_delete_an_entry(conn):
    response = r.db(DATABASE).table(TABLE).filter(r.row['name'] == 'General Troll').delete().run()

    assert response['deleted'] == 1

#EOF
