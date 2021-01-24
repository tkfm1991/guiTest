# coding: utf-8
import PySimpleGUI as sg
import logging


def create_gui(template):
    outer_layout = []
        
    for line in template:
        inner_layout = []
        for elem in line:
            for key, value in elem.items():
                print(key, value)

                if value == 'button':
                    # inner_layout.append(sg.Button(key))
                    inner_layout.append(create_button(key))
        
                if value == 'text':
                    # inner_layout.append(sg.Text(key))
                    inner_layout.append(create_text(key))
        outer_layout.append(inner_layout)
    
    return outer_layout


def create_button(elements):
    return sg.Button(elements)


def create_text(elements):
    return sg.Text(elements)


formatter = '%(asctime)s:%(message)s'
# logging.basicConfig(filename='log/guiTest.log', level=logging.DEBUG, format=formatter)
logging.basicConfig(level=logging.DEBUG, format=formatter)

win_height = 250
win_width = 200

main_template = [[{'メインメニュー': 'text'}],
    [{'設定': 'button'}],
    [{'追加': 'button'}],
    [{'終了': 'button'}]]

setting_template = [[{'設定': 'text'}],
    [{'テンプレート編集': 'button'}],
    [{'PW変更': 'button'}],
    [{'メインメニューへ戻る': 'button'}]]

main_layout = create_gui(main_template)
# ウィンドウ作成
main_window = sg.Window(title='Main Menu', size=(win_width, win_height)).Layout(main_layout)

while True:
    main_event , main_values = main_window.read()
    logging.debug(f'debug: [Event] {main_event}')

    if main_event == '設定':
        logging.debug('debug: 設定画面へ切替開始')
        setting_layout = create_gui(setting_template)
        setting_window = sg.Window(title='Setting', modal=True, size=(win_width, win_height)).Layout(setting_layout)
        logging.debug('debug: 設定画面へ切替終了')
        
        while True:
            setting_event, setting_values = setting_window.read()
            logging.debug(f'debug: [Event] {setting_event}')

            if setting_event in (None, 'メインメニューへ戻る'):
                logging.debug('debug: メイン画面へ切替開始')
                break

        setting_window.close()
        logging.debug('debug: メイン画面へ切替終了')

    if main_event == '追加':
        main_window.close()
        temp_template = main_template
        temp_template.append([{'TEST': 'button'}])
        main_template = temp_template

        layout = create_gui(main_template)
        main_window = sg.Window(title='Main Menu2', size=(win_width, win_height)).Layout(layout)

    if main_event in (None ,'終了'):
        logging.info(f'info: 終了します')
        break

main_window.close()