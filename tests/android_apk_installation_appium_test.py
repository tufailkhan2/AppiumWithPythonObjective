from Pages.android_apk_installation_appium import AndroidApkInstallationAppium
from basePackage.baseClass import BaseClass


class AndroidApkInstallationAppiumTest(BaseClass):

    def setUp(self):
        self.android_apk_installation_appium = AndroidApkInstallationAppium()
        self.android_apk_installation_appium.set_up()

    def test_click_app_button(self):
        self.android_apk_installation_appium.click_app_button()

    def tearDown(self):
        self.after_method()
