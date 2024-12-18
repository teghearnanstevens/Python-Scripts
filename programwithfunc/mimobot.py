from appium import webdriver
from time import sleep

# Desired capabilities for the Android device and app
desired_caps = {
    "platformName": "Android",  # Platform name (Android)
    "deviceName": "Avery's Note20 Ultra",  # Replace with your device name or ID (use adb devices to find this)
    "appPackage": "com.getmimo",  # Replace with the actual package name of the Mimo app
    "appActivity": ".MainActivity",  # Replace with the actual main activity of the Mimo app
    "noReset": True,  # Prevents the app from resetting its state
    "automationName": "UiAutomator2"  # Required for Android automation
}

# Connect to the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)

# Wait for the app to load
sleep(5)

try:
    # Example: Interact with the app
    print("Looking for the start lesson button...")
    button = driver.find_element("accessibility id", "Start Lesson")  # Replace with the correct selector
    button.click()
    sleep(2)

    # Example: Take a screenshot after interacting
    print("Taking a screenshot...")
    driver.save_screenshot('screenshot.png')

except Exception as e:
    # Handle errors gracefully
    print(f"An error occurred: {e}")

finally:
    # Quit the driver
    print("Quitting the driver...")
    driver.quit()
