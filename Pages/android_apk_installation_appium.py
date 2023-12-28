import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from utilities.utilitiesPage import PageUtils
from basePackage.baseClass import BaseClass


class AndroidApkInstallationAppium(BaseClass):

    def __init__(self):
        BaseClass.set_up()
        self.driver = BaseClass.get_driver()
        self.utilitiesPage = PageUtils()

    def click_app_button(self):
        appbutton = self.driver.find_element(By.ID, "android:id/button1")
        if appbutton is not None:
            appbutton.click()
            print("Test Executed")
        else:
            print("App element not found.")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Warp")').click()
        (self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                  'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Nigeria"));'
                                  ))

        class_name = "android.widget.TextView"

        # Find the list of elements by class name
        elements = self.driver.find_elements(AppiumBy.CLASS_NAME, class_name)

        # Initialize index variable
        index_of_nigeria = -1

        # Iterate through the elements and find the index of the element with text 'Nigeria'
        for index, element in enumerate(elements):
            # print("The text we got is: ", element.text)
            if element.text == 'Nigeria':
                index_of_nigeria = index
                break

        if index_of_nigeria != -1:
            print(f"The index of 'Nigeria' element is: {index_of_nigeria}")
        else:
            print("Element with text 'Nigeria' not found in the list.")

        box_ids = "com.mobeta.android.demodslv:id/drag_handle"
        list_elements = self.driver.find_elements(By.ID, box_ids)
        source = list_elements[index_of_nigeria - 1]
        target = list_elements[0]

        # Code for dragging Nigeria to top
        action = TouchAction(self.driver)
        action.long_press(source).move_to(target).release().perform()

        # Code for swiping Afghanistan to remove it from the list
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1294, 683)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(29, 689)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        class_name = 'android.widget.TextView'

        # Find all elements with the specified class
        text_view_elements = self.driver.find_elements(AppiumBy.CLASS_NAME, class_name)

        first_element_text = text_view_elements[1].text
        assert first_element_text == 'Nigeria'

        max_attempts = 30
        for i in range(max_attempts):

            # Check if there are any elements before attempting to get the text
            if text_view_elements:
                for element in text_view_elements:
                    element_text = element.text

                    # Add assertion to check if the text is not equal to 'Afghanistan'
                    assert element_text != 'Afghanistan'

                # Scroll down to load more elements
                size = self.driver.get_window_size()
                start_y = size['height'] * 0.8
                end_y = size['height'] * 0.2
                start_x = size['width'] * 0.5

                action = TouchAction(self.driver)
                action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()

                # Wait for a few seconds to allow the app to load more elements
                time.sleep(2)

                text_view_elements = self.driver.find_elements(AppiumBy.CLASS_NAME, class_name)
            else:
                print("No elements found with the specified class.")
                break

        #       Scenario two Navigate back to home screen.

        self.driver.back()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Multiple-choice mode")').click()
        checkboxes_element = "android.widget.CheckedTextView"
        self.utilitiesPage.click_random_checkboxes(checkboxes_element,5)

        self.checked_checkbox_texts = self.utilitiesPage.click_random_checkboxes(checkboxes_element,
                                                                                 5)
        print(self.checked_checkbox_texts)



