import pytest

from tests.functional.pages import MainPage
from tests.functional.utils import screenshot_on_failure

url = "http://localhost:8000"


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request):
    page = MainPage(browser, url)

    validate_title(page)
    validate_content(page)


def validate_title(page: MainPage):
    assert "mikepolo site" in page.title


def validate_content(page: MainPage):
    assert page.h1.tag_name == "h1"
    assert page.h1.text == "MIKEPOLO SITE"
    assert page.h2.tag_name == "h2"
    assert page.h2.text == "Welcome to"

    html = page.html
    assert "<hr>" in html
