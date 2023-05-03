import PySimpleGUI as sg
import os
import json

# Определяем путь к папке с программой
program_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем список последних выбранных программ
last_programs = ['', '', '']

# Загружаем список последних выбранных программ из файла, если он существует
last_programs_file = os.path.join(program_dir, 'last_programs.json')
if os.path.exists(last_programs_file):
    with open(last_programs_file, 'r') as f:
        last_programs = json.load(f)

# Создаем список типов файлов для отображения в диалоговом окне выбора файлов
filetypes = [("All files", "*.*")]

# Определяем графический интерфейс
layout = [
    [sg.Text("Select programs to run:")],
    [sg.InputText(last_programs[0], key='-PROGRAM1-', enable_events=True), sg.FileBrowse(file_types=filetypes)],
    [sg.InputText(last_programs[1], key='-PROGRAM2-', enable_events=True), sg.FileBrowse(file_types=filetypes)],
    [sg.InputText(last_programs[2], key='-PROGRAM3-', enable_events=True), sg.FileBrowse(file_types=filetypes)],
    [sg.Button("Run", key='-RUN-')]
]

# Создаем окно с графическим интерфейсом
window = sg.Window("KMA Runner", layout)

# Обрабатываем события окна
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-PROGRAM1-':
        last_programs[0] = values['-PROGRAM1-']
    elif event == '-PROGRAM2-':
        last_programs[1] = values['-PROGRAM2-']
    elif event == '-PROGRAM3-':
        last_programs[2] = values['-PROGRAM3-']
    elif event == '-RUN-':
        # Запускаем выбранные программы
        for program in last_programs:
            if program:
                os.startfile(program)
        
        # Сохраняем список последних выбранных программ в файл
        with open(last_programs_file, 'w') as f:
            json.dump(last_programs, f)
            
# Закрываем окно
window.close()
