---
- name: Изменение содержимого файла
  hosts: localhost
  tasks:
    - name: Добавить строку в начало файла
      lineinfile:
        path: /path/to/your/file
        line: 'model_path = "/path/to/model"'
        state: present
        insertbefore: BOF  # Вставляет строку в начало файла

    - name: Заменить все строки ".." на "{model_path}"
      replace:
        path: /path/to/your/file
        regexp: '^\.\.$'  # Регулярное выражение для строки ".."
        replace: '{model_path}'