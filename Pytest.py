import main
import pytest

g = main.Zenportal_login()

# test for login to Zenportal_login
@pytest.mark.first
def test_login():
    g.login()
    assert g.driver.current_url == "https://www.zenclass.in/class"

@pytest.mark.second
def test_createquery():
    g.queue()
