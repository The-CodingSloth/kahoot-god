import keyboard
import pyautogui
import pytesseract
import openai

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe example path: r"C:\Program Files\Tesseract-OCR\tesseract.exe"
openai.api_key = "YOUR_API_KEY"


def click_button(button):
    # Coordinates for each button
    button_coords = {1: (579, 1040), 2: (1562, 1037), 3: (528, 1261), 4: (1803, 1255)}
    x, y = button_coords[button]
    pyautogui.click(x, y)


def chatGPT_answer(question_and_answers):
    # Adding explicit instruction to the prompt
    # Modify the instruction to the model to fit your needs
    conversation = [
        {
            "role": "system",
            "content": "You are a helpful assistant specialized in answering multiple-choice questions who only responds with the button number corresponding to the most likely answer do not respond with words only a integer. You'll do this even if the question involves content you can't analyze, such as videos or images. If you cannot answer the question, you'll respond with an educated guess. Remember only respond with an integer between 1 and 4 that corresponds to the answer.",
        },
        {"role": "user", "content": question_and_answers},
    ]
    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation) # can be set to 'gpt-4' if needed

        # Extract the assistant's reply
        reply = response["choices"][0]["message"]["content"].strip()
        # Return the button number as an integer
        return int(reply)
    except ValueError:
        # Handle exception here if the reply is not an integer
        print(f"Unexpected reply: {reply}")
        return int(reply[0])
    except:
        # Handle exception here if something else goes wrong
        print("Something went wrong.")
        print(response)
        return None


def kahoot_god():
    # Coordinates for kahoot question and answers
    question_and_answers = {
        0: {"top_left": (0, 72), "bottom_right": (2475, 200)},
        1: {"top_left": (105, 1000), "bottom_right": (1219, 1118)},
        2: {"top_left": (1370, 1000), "bottom_right": (2500, 1127)},
        3: {"top_left": (100, 1200), "bottom_right": (1260, 1361)},
        4: {"top_left": (1370, 1175), "bottom_right": (2000, 1353)},
    }
    res = ""
    for element in question_and_answers:
        coords = question_and_answers[element]
        x1, y1 = coords["top_left"]
        x2, y2 = coords["bottom_right"]

        # Calculate width and height for each element for screenshot
        width = x2 - x1
        height = y2 - y1

        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        screenshot_text = pytesseract.image_to_string(screenshot)
        if not screenshot_text.strip():
            print("No text detected.")
            continue
        if element == 0:
            res += f"Question: {screenshot_text}"
        else:
            res += f"{element}: {screenshot_text}"
    print(res)
    try:
        answer = chatGPT_answer(res)
        click_button(answer)
        print(f"Answer: {answer}")
    except:
        print("chatGPT_answer failed")


# Bind the function to a hotkey
keyboard.add_hotkey("ctrl+alt+t", kahoot_god)
# Keep the program running
keyboard.wait()
