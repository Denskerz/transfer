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

    - name: Заменить строки с использованием цикла
      replace:
        path: /path/to/your/file
        regexp: "{{ item.regexp }}"
        replace: "{{ item.replace }}"
      loop:
        - { regexp: '=\s*f?"(\.\./shshsj)"', replace: '= f"{model_path}/shshsj"' }
        - { regexp: 'ansi', replace: 'cp1251' }
        - { regexp: '«,', replace: '«.' }