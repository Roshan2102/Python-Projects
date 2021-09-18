'''
The task is to create a language translator using library the google trans.
'''
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
# root.iconbitmap("Iconmoon-Web-Application-Profile")
root.geometry('1080x350')
root.resizable(0, 0)
root.title("Language Translator")
root.config(bg='ghost white')

# heading
Label(root, text=" ROSHAN LANGUAGE TRANSLATOR",
      font="arial 20 bold", bg='white smoke').pack()


# TEXT WIDGET
Label(root, text="Enter Text", font='arial 13 bold',
      bg='white smoke').place(x=200, y=60)
Input_text = Text(root, font='arial 10', height=11,
                  wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)


Label(root, text="Output", font='arial 13 bold',
      bg='white smoke').place(x=780, y=60)
Output_text = Text(root, font='arial 10', height=11,
                   wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

### DropDown  #####
language = list(LANGUAGES.values())

input_lang = ttk.Combobox(root, values=language, width=25)
input_lang.place(x=20, y=60)
input_lang.set('choose input language')

trans_lang = ttk.Combobox(root, values=language, width=25)
trans_lang.place(x=890, y=60)
trans_lang.set('choose output language')

#######  function that translate the text #######


def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(
        1.0, END), src=input_lang.get(), dest=trans_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

#########  Translate Button ########


trans_btn = Button(root, text='Translate', font='arial 12 bold', fg="white",
                   pady=5, command=Translate, bg='blue', activebackground='sky blue')
trans_btn.place(x=490, y=180)


root.mainloop()
