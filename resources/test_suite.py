import pytest
from tests.test_android_apk_installation_appium import AndroidApkInstallationAppiumTest


@pytest.fixture()
def android_app(request):
    android_app = AndroidApkInstallationAppiumTest()
    android_app.setUp()
    yield android_app
    android_app.after_method()


def test_click_app_button(android_app):
    android_app.test_click_app_button()
