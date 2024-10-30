import math
import os
import random
import sys
import time
import cv2
import keyboard
import mss
import numpy as np
import pygetwindow as gw
import win32api
import win32con

from colorama import Fore, Style, init

# Инициализация приоритетов
PRIORITY_OBJECTS = {
    "bomb": (0, 0, 0),    # Примерный HSV для бомбы (чёрный или серый)
    "pigeon": (90, 50, 200),  # Примерный HSV для голубя (голубоватый)
    "pumpkin": (10, 150, 150)  # HSV для тыквы (оранжевый оттенок)
}
def get_priority(object_name):
    """Возвращает приоритет для сортировки: меньшее значение - более высокий приоритет."""
    priorities = {"bomb": 1, "pigeon": 2, "pumpkin": 3}
    return priorities.get(object_name, 999)

# Инициализация для Windows
init(autoreset=True)

def resource_path(relative_path):
    """ Load images for .exe """
    try:
        base_path = sys._MEIPASS
        return str(os.path.join(base_path, relative_path))
    except Exception:
        return relative_path

class Logger:
    def __init__(self, prefix=None):
        self.prefix = prefix

    def log(self, data: str, color=None):
        # Всегда окрашиваем заголовок ">>>    https://t.me/CryptoSpy_news  <<<   " в цвет
        if self.prefix == ">>>    https://t.me/CryptoSpy_news  <<<   ":
            print(f"{Fore.CYAN}{self.prefix}{Style.RESET_ALL} {data}")
        else:
            color = color if color else ""
            print(f"{color}{self.prefix} {data}")

    def input(self, text: str, color=None):
        # Окрашиваем заголовок для метода input так же, как и для log
        if self.prefix == ">>>    https://t.me/CryptoSpy_news  <<<   ":
            return input(f"{Fore.CYAN}{self.prefix}{Style.RESET_ALL} {text}")
        else:
            color = color if color else ""
            return input(f"{color}{self.prefix} {text}")

class AutoClicker:
    def __init__(self, window_title, target_colors_hex, nearby_colors_hex, logger, percentages: float,
                 is_continue: bool):
        self.window_title = window_title
        self.target_colors_hex = target_colors_hex
        self.nearby_colors_hex = nearby_colors_hex
        self.logger = logger
        self.running = False
        self.clicked_points = []
        self.iteration_count = 0

        self.percentage_click = percentages
        self.is_continue = is_continue

        self.target_hsvs = [self.hex_to_hsv(color) for color in self.target_colors_hex]
        self.nearby_hsvs = [self.hex_to_hsv(color) for color in self.nearby_colors_hex]

        self.templates_plays = [
            cv2.cvtColor(cv2.imread(img, cv2.IMREAD_UNCHANGED), cv2.COLOR_BGRA2GRAY) for img in CLICK_IMAGES
        ]  # click image

    @staticmethod
    def hex_to_hsv(hex_color):
        hex_color = hex_color.lstrip('#')
        h_len = len(hex_color)
        rgb = tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len // 3))
        rgb_normalized = np.array([[rgb]], dtype=np.uint8)
        hsv = cv2.cvtColor(rgb_normalized, cv2.COLOR_RGB2HSV)
        return hsv[0][0]

    @staticmethod
    def click_at(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def toggle_script(self):
        self.running = not self.running
        r_text = "ON" if self.running else "OFF"
        self.logger.log(f'Status: {r_text}')

    def is_near_color(self, hsv_img, center, target_hsvs, radius=8):
        x, y = center
        height, width = hsv_img.shape[:2]
        for i in range(max(0, x - radius), min(width, x + radius + 1)):
            for j in range(max(0, y - radius), min(height, y + radius + 1)):
                distance = math.sqrt((x - i) ** 2 + (y - j) ** 2)
                if distance <= radius:
                    pixel_hsv = hsv_img[j, i]
                    for target_hsv in target_hsvs:
                        if np.allclose(pixel_hsv, target_hsv, atol=[1, 50, 50]):
                            return True
        return False

    def find_and_click_image(self, template_gray, screen, monitor):
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGRA2GRAY)

        result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.7:
            template_height, template_width = template_gray.shape
            center_x = max_loc[0] + template_width // 2 + monitor["left"]
            center_y = max_loc[1] + template_height // 2 + monitor["top"]
            self.click_at(center_x, center_y)
            return True

        return False

    def click_color_areas(self):
        windows = gw.getWindowsWithTitle("TelegramDesktop")
        if not windows:
            self.logger.log(f"Не найдено окна с заголовком: {self.window_title}")
            all_windows = gw.getAllTitles()
            self.logger.log(f"Все открытые окна: {all_windows}")
            return

        try:
            window = windows[0]
            if window.isActive:
                self.logger.log("Окно уже активно")
            else:
                window.activate()
        except Exception as e:
            self.logger.log(f"Ошибка при активации окна: {str(e)}")
            return

        self.logger.log("Игра началась")  # Уведомление о начале игры

        with mss.mss() as sct:
            grave_key_code = 41
            keyboard.add_hotkey(grave_key_code, self.toggle_script)

            while True:
                if self.running:
                    monitor = {
                        "top": window.top,
                        "left": window.left,
                        "width": window.width,
                        "height": window.height
                    }
                    img = np.array(sct.grab(monitor))
                    img_bgr = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

                    detected_objects = []  # Список найденных объектов для сортировки по приоритету

                    for obj_name, target_hsv in PRIORITY_OBJECTS.items():
                        lower_bound = np.array([max(0, target_hsv[0] - 10), 80, 80])
                        upper_bound = np.array([min(179, target_hsv[0] + 10), 255, 255])
                        mask = cv2.inRange(hsv, lower_bound, upper_bound)

                        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                        for contour in contours:
                            if cv2.contourArea(contour) < 8:
                                continue

                            M = cv2.moments(contour)
                            if M["m00"] == 0:
                                continue

                            cX = int(M["m10"] / M["m00"]) + monitor["left"]
                            cY = int(M["m01"] / M["m00"]) + monitor["top"]

                            detected_objects.append((obj_name, cX, cY))

                    # Сортировка объектов по приоритету
                    detected_objects.sort(key=lambda x: get_priority(x[0]))

                    # Клик на объекты в порядке приоритета
                    for obj_name, cX, cY in detected_objects:
                        if any(math.sqrt((cX - px) ** 2 + (cY - py) ** 2) < 35 for px, py in self.clicked_points):
                            continue

                        cY += 7  # Корректировка Y
                        self.click_at(cX, cY)
                        self.clicked_points.append((cX, cY))

                    time.sleep(0.222)
                    self.iteration_count += 1
                    if self.iteration_count >= 5:
                        self.clicked_points.clear()
                        if self.is_continue:
                            for tp in self.templates_plays:
                                self.find_and_click_image(tp, img, monitor)
                        self.iteration_count = 0


if __name__ == "__main__":
    # Инициализируем Logger с вашим заголовком
    logger = Logger(">>>    https://t.me/CryptoSpy_news  <<<   ")

    # Выводим логи
    logger.log("Этот скрипт работает на базе обучаемой модели OpenCV — мощной библиотеки для компьютерного зрения. Во время игры скрипт имитирует поведение реального игрока, за счет работы девайсов - перемещение курсора мыши и нажатия клавиш.")
    
    # Остальная логика программы
    CLICK_IMAGES = [resource_path("media\\lobby-play.png"), resource_path("media\\continue-play.png")]

    PERCENTAGES = {
        "1": 0.13,  # 100 очков
        "2": 0.17,  # 150 очков
        "3": 0.235,  # 175 очков
        "4": 1,
    }

    # Запрос количества очков
    answer = None
    while answer is None:
        points_key = logger.input(
            "Сколько очков хотите добыть? | 1 -> Простая разминка (90-110) | 2 -> Серьезный вызов (140-160) | 3 -> Почти на вершине (170-180) | 4 -> Максимум очков!: ")
        answer = PERCENTAGES.get(points_key, None)
        if answer is None:
            logger.log("Неверное значение", color=Fore.RED)
    percentages = answer

    # Запрос автоматического 'Play'
    answer = None
    answs = {
        "1": True,
        "0": False
    }
    while answer is None:
        points_key = logger.input("Активировать автоматический запуск игры? | 1 - Да / 0 - Нет: ")
        answer = answs.get(points_key, None)
        if answer is None:
            logger.log("Неверное значение", color=Fore.RED)
    is_continue = answer

    logger.log('Перед началом игры нажмите клавишу "ё" (`) на клавиатуре, чтобы активировать режим автокликера.', color=Fore.YELLOW)

    # Остальная логика программы
    target_colors_hex = ["#e37932", "#e37b33"]
    nearby_colors_hex = ["#e99b66", "#c35f27"]
    auto_clicker = AutoClicker("TelegramDesktop", target_colors_hex, nearby_colors_hex, logger, percentages=percentages, is_continue=is_continue)

    try:
        auto_clicker.click_color_areas()
    except Exception as e:
        logger.log(f"Произошла ошибка: {e}", color=Fore.RED)
    
    for i in reversed(range(5)):
        i += 1
        print(f"Скрипт завершит работу через {i}")
        time.sleep(1)
