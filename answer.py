---
- name: Изменение содержимого файла
  hosts: localhost
  vars:
    workdir: /path/to/your  # Задайте значение переменной workdir здесь

  tasks:
    - name: Добавить строку в начало файла
      lineinfile:
        path: "{{ workdir }}/file"
        line: 'model_path = "/path/to/model"'
        state: present
        insertbefore: BOF  # Вставляет строку в начало файла

    - name: Заменить строки с использованием цикла
      replace:
        path: "{{ workdir }}/file"
        regexp: "{{ item.regexp }}"
        replace: "{{ item.replace }}"
      loop:
        - { regexp: '=\s*f?"(\.\./shshsj)"', replace: '= f"{model_path}/shshsj"' }
        - { regexp: 'ansi', replace: 'cp1251' }
        - { regexp: '«,', replace: '«.' }
        - { regexp: '^input_filepath.*$', replace: '«hello»' }  # Заменяет строку input_filepath на «hello»

    - name: Обработать input_filepath и output_filepath
      block:
        - name: Добавить строку {{ item }} если её нет
          lineinfile:
            path: "{{ workdir }}/file"
            line: "{{ item.line }}"
            state: present
          when: >
            not (lookup('file', '{{ workdir }}/file').find(item.check) != -1)
          loop:
            - { line: 'input_filepath = f"../shshsj"', check: 'input_filepath = f"../shshsj"' }
            - { line: 'output_filepath = f"../output"', check: 'output_filepath = f"../output"' }