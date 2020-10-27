from googletrans import Translator
import keyboard
import pyperclip



def ceviri():
    trans = Translator()

    yazi = pyperclip.paste()


    t = trans.translate(
            yazi,dest='tr'
        )

    i = trans.translate(
        yazi,dest='en'
    )
    print(f'{i.text} {t.text}')
    if t.src == 'en':
        pyperclip.copy(t.text)

    if i.src == 'tr':
        pyperclip.copy(i.text)

    
keyboard.add_hotkey('tab', lambda: ceviri())

keyboard.wait()