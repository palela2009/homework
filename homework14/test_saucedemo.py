import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def login(self, username, password):
        username_input = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()

    def logout(self):
        menu_button = self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_button.click()
        logout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_button.click()

    def test_locked_out_user(self):
        self.login("locked_out_user", "secret_sauce")
        try:
            error_container = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
            print("Locked Out User Error:", error_container.text)
        except:
            self.logout()

    def test_performance_glitch_user(self):
        self.login("performance_glitch_user", "secret_sauce")
        try:
            error_container = self.driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")
            if error_container:
                print("Performance Glitch Error:", error_container[0].text)
            else:
                self.logout()
        except Exception as e:
            print("An error occurred during performance test:", str(e))

    def test_problem_user(self):
        self.login("problem_user", "secret_sauce")
        try:
            error_container = self.driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")
            if error_container:
                print("Problem User Error at Login:", error_container[0].text)
                return

            add_buttons = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
            add_buttons[0].click()
            add_buttons[1].click()

            remove_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_secondary")
            for button in remove_buttons:
                button.click()

            self.logout()
        except Exception as e:
            print("Problem User Action Failed:", str(e))
            try:
                self.logout()
            except:
                pass

    def test_standard_user(self):
        self.login("standard_user", "secret_sauce")
        try:
            error_container = self.driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")
            if error_container:
                print("Standard User Error at Login:", error_container[0].text)
                return

            add_buttons = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
            add_buttons[0].click()
            add_buttons[1].click()

            time.sleep(5)

            remove_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_secondary")
            if remove_buttons:
                remove_buttons[0].click()

            item_link = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name")))
            item_link.click()

            time.sleep(5)

            self.driver.back()

            sort_select = Select(
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))))
            sort_select.select_by_value("hilo")

            facebook_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Facebook")))
            facebook_link.click()

            windows = self.driver.window_handles
            if len(windows) > 1:
                self.driver.switch_to.window(windows[1])
                self.driver.close()
                self.driver.switch_to.window(windows[0])

            linkedin_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "LinkedIn")))
            linkedin_link.click()

            windows = self.driver.window_handles
            if len(windows) > 1:
                self.driver.switch_to.window(windows[1])
                self.driver.close()
                self.driver.switch_to.window(windows[0])

            self.logout()

        except Exception as e:
            print("Standard User Action Failed:", str(e))


if __name__ == "__main__":
    unittest.main()