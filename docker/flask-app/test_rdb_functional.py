# These are the functional tests for the database connection

import pytest


@pytest.fixture(scope='session')
def conn(request):
    conn = webdriver.Firefox(capabilities=caps)
    def fin():
        conn.quit()
    request.addfinalizer(fin)
    return conn

# The app gets a request to call something from the database
# so it requests a connection.
