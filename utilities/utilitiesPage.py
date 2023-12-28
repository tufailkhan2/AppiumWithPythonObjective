import random
from selenium.webdriver.common.by import By
from basePackage.baseClass import BaseClass


class PageUtils(BaseClass):

    def __init__(self):
        pass

    def click_random_checkboxes(self, checkboxes_locator, number_of_checkboxes_to_click):
        checkboxes = self.get_driver().find_elements(By.CLASS_NAME, checkboxes_locator)

        # Validate input
        if not checkboxes:
            print(f'No checkboxes found with the provided locator')
            return

        # Ensure the number of checkboxes to click is within bounds
        number_of_checkboxes_to_click = min(number_of_checkboxes_to_click, len(checkboxes))

        # Shuffle the list of checkboxes to randomize checkbox selection
        shuffled_checkboxes = random.sample(checkboxes, len(checkboxes))

        checked_checkbox_texts = []
        checked_indices = []

        # Click the specified number of checkboxes
        for checkbox in shuffled_checkboxes[:number_of_checkboxes_to_click]:
            checkbox.click()
            checked_checkbox_texts.append(checkbox.text)

        print(checked_checkbox_texts)

        elements_checked = self.get_driver().find_elements(By.CLASS_NAME, 'android.widget.CheckedTextView')
        checked_indices = [index for index, element in enumerate(elements_checked) if element.text in
                           checked_checkbox_texts]
        print('The indices returned are: ', checked_indices)

        delete_icon_class = 'android.widget.ImageView'

        delete_icons = self.get_driver().find_elements(By.CLASS_NAME, delete_icon_class)

        for index in checked_indices:
            if 0 <= index < len(delete_icons):
                delete_icon = delete_icons[index+1]
                delete_icon.click()
                # Perform any other actions you need on the delete icon
            else:
                print(f"Index {index} is out of bounds.")

        return checked_checkbox_texts

