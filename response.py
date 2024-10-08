import curses

def main(stdscr):
    # Очищаем экран
    stdscr.clear()
    
    # Начальный текст
    text = "Редактируйте этот текст и нажмите F9 для сохранения."
    
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, text)
        stdscr.addstr(2, 0, "Нажмите F9 для сохранения и выхода")
        stdscr.addstr(3, 0, "Нажмите F10 для выхода без сохранения")

        # Обновляем экран
        stdscr.refresh()

        # Получаем ввод от пользователя
        key = stdscr.getch()

        # Обработка клавиш
        if key == curses.KEY_BACKSPACE or key == 127:
            text = text[:-1]  # Удаляем последний символ
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break  # Завершаем редактирование
        elif key in (curses.KEY_F9, ord('s')):  # Сохранение
            with open('output.txt', 'w') as f:
                f.write(text)
            break
        elif key in (curses.KEY_F10, ord('q')):  # Выход без сохранения
            break
        else:
            text += chr(key)  # Добавляем введенный символ

if __name__ == "__main__":
    curses.wrapper(main)
