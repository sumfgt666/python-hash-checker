import PySimpleGUI as sg
import hashlib

blockSize = 65536
layout = [
    [sg.Text('File: '), sg.InputText(), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Text('Hash:'), sg.InputText()],
    [sg.Text('')],
    [sg.Radio('MD5', "RADIO1"), sg.Radio('SHA1', "RADIO1"), sg.Radio('SHA256', "RADIO1")],
    [sg.Output(size=(88, 20))],
    [sg.Submit()]
]

window = sg.Window('Hash Checker', layout)


while True:                             # The Event Loop
    event, values = window.read()

    if event == 'Submit':
        if values[0] == '':
            print('Error: No file selected. Please select a file and try again.\n')
        else:
            for i in values:
                if values[i] is True:
                    hashType = i

            if hashType == 2:
                hasher = hashlib.md5()
            elif hashType == 3:
                hasher = hashlib.sha1()
            elif hashType == 4:
                hasher = hashlib.sha256()
            else:
                print('Error: No hash selected. Please select a hash and try again.\n')

            try:
                with open(values[0], 'rb') as a:
                    buf = a.read(blockSize)

                    while len(buf) > 0:
                        hasher.update(buf)
                        buf = a.read(blockSize)
            except:
                print('Error: Broken file path. Please try re-selecting a file and try again.\n')
                break

            values[1] = values[1].lower()

            if hasher.hexdigest() != values[1]:
                print('Warning: Input hash does not match file hash.\nInput file: ' + values[0] + '\nFile hash: ' + str(hasher.hexdigest()) + '\nInput hash: ' + str(values[1]) + '\n')
            elif hasher.hexdigest() == values[1]:
                print('Success! The input hash matches the file hash.\nInput file: ' + values[0] + '\nFile hash: ' + str(hasher.hexdigest()) + '\nInput hash: ' + str(values[1]) + '\n')

    if event in (None, 'Exit', 'Cancel'):
        break
