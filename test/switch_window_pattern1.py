# 画面切替
# メイン画面⇔サブ画面を切替（サブ画面を閉じたらメイン画面が開く）

import PySimpleGUI as sg

win_height = 150
win_width = 200
main_layout = [[sg.Text('Main Window')],
    [sg.OK()]]
main_window = sg.Window(title='Main', size=(win_width, win_height)).Layout(main_layout)

while True:
    main_event, main_value = main_window.read()

    if main_event is None:
        break

    elif main_event == 'OK':
        sub_layout = [[sg.Text('Sub Window')],
            [sg.Cancel()]]
        sub_window = sg.Window(title='Sub', size=(win_width, win_height)).Layout(sub_layout)
        main_window.close()

        while True:
            sub_event, sub_value = sub_window.read()

            if sub_event in (None, 'Cancel'):
                main_layout = [[sg.Text('Main Window')],
                    [sg.OK()]]
                main_window = sg.Window(title='Main', size=(win_width, win_height)).Layout(main_layout)
                break

        sub_window.close()

main_window.close()