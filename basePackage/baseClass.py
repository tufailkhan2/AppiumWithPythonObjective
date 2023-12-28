from appium import webdriver
from appium.options.android import UiAutomator2Options


class BaseClass:
    driver = None

    @classmethod
    def set_up(cls):
        if cls.driver is None:
            desired_caps_default = {
                'platformName': 'Android',
                'automationName': 'UiAutomator2',
                'platformVersion': '9.0',
                'deviceName': 'Android Emulator',
                'app': r"C:\\Users\\Tufail Khan\\PycharmProjects\\AppiumWithPythonProject\\apps\\draganddrop.apk"
            }
            capabilities_options = UiAutomator2Options().load_capabilities(desired_caps_default)
            cls.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", options=capabilities_options)

    @classmethod
    def get_driver(cls):
        return cls.driver

    @classmethod
    def after_method(cls):
        if cls.driver is not None:
            cls.driver.quit()

