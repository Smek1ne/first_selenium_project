import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='type your lang')


@pytest.fixture()
def browser(request):
    options = Options()
    language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()