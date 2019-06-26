import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose a language to start your browser with: en, ru, es, fr etc.')


@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    languages = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': languages})
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


