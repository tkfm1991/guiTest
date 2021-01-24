# 画面切替
# メイン画面⇔サブ画面を切替（メイン画面でもサブ画面を閉じても終了）

import PySimpleGUI as sg

win_height = 150
win_width = 200

main_layout = [[sg.Text('Main Window')],
    [sg.OK()]]

sub_layout = [[sg.Text('Sub Window')],
    [sg.Cancel()]]


window = sg.Window(title='Main', size=(win_width, win_height), keep_on_top = False).Layout(main_layout)

while True:
    event, value = window.read()

    if event is None:
        break

    elif event == 'OK':
        window.close()
        # sub_layout = [[sg.Text('Sub Window')],
        #     [sg.Cancel()]]
        sub_layout_temp = sub_layout
        window = sg.Window(title='Sub', size=(win_width, win_height), keep_on_top = False).Layout(sub_layout_temp)

    elif event == 'Cancel':
        window.close()
        main_layout = [[sg.Text('Main Window')],
            [sg.OK()]]
        window = sg.Window(title='Main', size=(win_width, win_height), keep_on_top = False).Layout(main_layout)

window.close()