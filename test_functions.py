import keyboard
import pyautogui
import pytesseract


"""
Use this snippet to get the coordinates of the mouse cursor to help you get the coordinates for your screenshots.
pyautogui.moveTo(0, 0)
while True:
    x, y = pyautogui.position()
    print(f"X: {x}, Y: {y}", end="\r")
"""
# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = ""  # Path to tesseract.exe example path: r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def test_screenshots_of_buttons():
    # Coordinates for each button
    button_coords = {
        0: {"top_left": (0, 72), "bottom_right": (2475, 200)},
        1: {"top_left": (105, 1000), "bottom_right": (1219, 1118)},
        2: {"top_left": (1370, 1000), "bottom_right": (2500, 1127)},
        3: {"top_left": (100, 1200), "bottom_right": (1260, 1361)},
        4: {"top_left": (1370, 1175), "bottom_right": (2000, 1353)},
    }

    for button in button_coords:
        coords = button_coords[button]
        x1, y1 = coords["top_left"]
        x2, y2 = coords["bottom_right"]

        # Calculate width and height
        width = x2 - x1
        height = y2 - y1

        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        screenshot_path = f"screenshot_button_{button}.png"
        screenshot.save(screenshot_path)
        # Open the screenshot
        # os.system(
        #   f"start {screenshot_path}"
        # )  # Use "xdg-open" on Linux, "start" on Windows


def ocr_test():
    # Coordinates for each button
    button_coords = {
        0: {"top_left": (0, 72), "bottom_right": (2475, 200)},
        1: {"top_left": (105, 1000), "bottom_right": (1219, 1118)},
        2: {"top_left": (1370, 1000), "bottom_right": (2500, 1127)},
        3: {"top_left": (100, 1200), "bottom_right": (1260, 1361)},
        4: {"top_left": (1370, 1175), "bottom_right": (2000, 1353)},
    }

    for button in button_coords:
        coords = button_coords[button]
        x1, y1 = coords["top_left"]
        x2, y2 = coords["bottom_right"]

        # Calculate width and height
        width = x2 - x1
        height = y2 - y1

        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        screenshot_text = pytesseract.image_to_string(screenshot)
        if screenshot_text.strip() == "a\\":
            print("No text detected.")
            continue
        if not screenshot_text.strip():
            print("No text detected.")
            continue
        print(f"Text for button {button}: {screenshot_text}")


# Bind the function to a hotkey (e.g., Ctrl+Alt+T)
keyboard.add_hotkey("ctrl+alt+t", test_screenshots_of_buttons)
# Keep the program running
keyboard.wait()
