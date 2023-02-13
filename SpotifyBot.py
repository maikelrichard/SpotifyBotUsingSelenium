import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://accounts.spotify.com/en/login")

# Wait for the username field to load and enter the username
wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
username.click()
username.send_keys("matttaylornz@gmail.com")

# Wait for the password field to load and enter the password
wait = WebDriverWait(driver, 10)
password = wait.until(EC.presence_of_element_located((By.ID, "login-password")))
password.click()
password.send_keys("taylor02")

# Wait for the login button to load and click it
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
login_button.click()

time.sleep(5)

driver.get("https://open.spotify.com/album/0mCWqN0VvChqQh8ITK92W4")

# Wait for the play button to load and click it
wait = WebDriverWait(driver, 10)
play_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > div > button")))
play_button.click()

human_timeout = 60

for i in range(10):
    print("Song Playing...")
    time.sleep(human_timeout)
    play_button.click()

driver.quit()
