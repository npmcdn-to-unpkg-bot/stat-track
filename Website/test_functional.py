# These are the functional tests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities \
        import DesiredCapabilities

caps  = DesiredCapabilities.FIREFOX
caps['marionette'] = True

import pytest


@pytest.fixture(scope='session')
def browser(request):
    browser = webdriver.Firefox(capabilities=caps)
    def fin():
        browser.quit()
    request.addfinalizer(fin)
    return browser


def test_can_start_a_chart(browser):
    # Jon has heard about a cool new online app to track real-time
    # twitter keyword statistics. He goes to check out the homepage.
    browser.get('http://localhost:5000')


    # He notices the page title and header mention twitter statistics
    assert '' in browser.title


    # He is invited to enter a keyword and see its activity straightaway.
        # assert False, 'Finish the tests'


    # He types 'Obama' into a text box (Jon likes to follow politics).


    # When he hits enter, the page updates, and now the page displays
    # a chart that shows frequency of tweets.


    # Upon closer inspection, Jon notices that the chart is updating in
    # real-time.


    # Jon wonders whether the site will show another chart if he searches
    # for a different keyword. There is some explanatory text
    # to that effect.


    # He types in a new word and the site displays a new chart.


    # Satisfied, he goes to grab lunch.



