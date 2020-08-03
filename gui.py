import PySimpleGUI as sg

# sg.theme_previewer()
sg.theme('DarkTeal12')

# TODO добавить папку по умолчанию \ текущая директория
layout = [[sg.Text('1) Выбрать папку для выгрузки'), sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.FolderBrowse('Выбрать', key='-IN-')],
          [sg.Button('Выгрузить')],
          [sg.Text('2) Выбрать проект который следует установить')],
          [sg.Combo(['Проект 1', 'Проект 2'], size=(45, 1), readonly=True)],
          [sg.Text('3) Выбрать период работы')],

          [sg.Input(size=(9, 1), key='-DATE_IN-', readonly=True),
           sg.CalendarButton('Начало', begin_at_sunday_plus=1, key='-TXT_DATE_IN-', format='%Y:%m:%d')],

          [sg.Input(size=(9, 1), key='-DATE_OUT-', readonly=True),
           sg.CalendarButton('Конец', begin_at_sunday_plus=1, key='-TXT_DATE_OUT-', format='%Y:%m:%d')],

          [sg.Text('4) Выбрать тип занятости')],
          [sg.Combo(['Ставка:', 'Оклад:', 'Выход:', 'За час:'], ['Ставка:'], size=(7, 1), readonly=True),
           sg.Input('0.00', size=(9, 1), key='-TYPE-', justification='r'),
           sg.Check('Автосогласование доп. работ')],

          [sg.Text('3) Выбрать файл для загрузки')]
          ]

# layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
#           [sg.Input(key='-IN-')],
#           [sg.Button('Show'), sg.Button('Exit')]]
#
window = sg.Window('Массовое назначение мерчей', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    # if event == '-DATE_IN-':
    #     window['-TXT_DATE_IN-'].update(values['-DATE_IN-'])
    # if event == '-DATE_OUT-':
    #     window['-TXT_DATE_OUT-'].update(values['-DATE_OUT-'])
    if event == '-IN-':
        window['-OUTPUT-'].update(values['-IN-'])
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Выгрузить':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
