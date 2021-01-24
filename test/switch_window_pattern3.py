# 画面切替
# サブ画面を別ウインドウで開く

import PySimpleGUI as sg

win_height = 150
win_width = 200
main_layout = [[sg.Text('Main Window')],
    [sg.OK()]]
main_window = sg.Window(title='Main', size=(win_width, win_height)).Layout(main_layout)

while True:
    main_event, main_value = main_window.read()
    print(f'Event: {main_event}, Value: {main_value}')

    if main_event is None:
        break

    elif main_event == 'OK':
        sub_layout = [[sg.Text('Sub Window')],
            [sg.Cancel()]]
        # modal: Subウインドウが閉じられるまではMain側の操作を無効にする
        sub_window = sg.Window(title='Sub', modal=True, size=(win_width, win_height)).Layout(sub_layout)
        # main_window.close()

        while True:
            sub_event, sub_value = sub_window.read()
            print(f'Event: {sub_event}, Value: {sub_value}')

            if sub_event in (None, 'Cancel'):
                break

        sub_window.close()

main_window.close()