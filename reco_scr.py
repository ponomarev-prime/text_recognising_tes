import cv2
import pytesseract

def recognize_text(screen_region):
    # Захватываем выбранный участок экрана
    screenshot = cv2.cvtColor(screen_region, cv2.COLOR_BGR2RGB)

    # Преобразуем изображение в текст с помощью pytesseract
    text = pytesseract.image_to_string(screenshot)

    # Выводим распознанный текст в терминал
    print(text)

# Захватываем выбранный участок экрана с помощью OpenCV
# Убедитесь, что выбранный участок экрана находится внутри экрана
screen_region = cv2.imread("screenshot.png")

# Вызываем функцию распознавания текста
recognize_text(screen_region)
