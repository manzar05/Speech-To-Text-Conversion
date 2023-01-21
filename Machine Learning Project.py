# Importing all the necessary modules
from tkinter.messagebox import showinfo
import pyttsx3
import speech_recognition as sr
from tkinter import *
from PIL import ImageTk,Image

# Creating the python text to speech and speech to text functions
def speak(text: str):
    engine = pyttsx3.init()
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    # Use female English voice
    engine.setProperty('voice', en_voice_id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',0.9)
    engine.say(text)
    engine.runAndWait()

def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language="en-IN")
        except Exception as e:
            showinfo(title='Error!', message=e)
            speak("I am sorry, I did not get that, but could you please repeat that")

            return "Nothing"
        return query

# Creating the main TTS and STT functions and the instruction functions
def TTS():
    tts_wn = Toplevel(root)
    tts_wn.title('Text-to-Speech Converter')
    tts_wn.geometry("500x400")
    tts_wn.configure(bg='#a3ffb4')

    Label(tts_wn, text='Text-to-Speech Converter', font=("Candara", 16),fg='#473126', bg='#a3ffb4').place(x=130,y=50)

    text = Text(tts_wn, height=10, width=35, font=8)
    text.place(x=50, y=80)

    speak_btn = Button(tts_wn, text='Hear',font=("Candara", 16), bg='#fff68f', command=lambda: speak(str(text.get(1.0, END))))
    speak_btn.place(x=230, y=330)

def STT():
    stt_wn = Toplevel(root)
    stt_wn.title('Speech-to-Text Converter')
    stt_wn.geometry("500x400")
    stt_wn.configure(bg='#7fdcec')

    Label(stt_wn, text='Speech-to-Text Converter', font=("Candara", 16),fg='#3e5020', bg='#7fdcec').place(x=130,y=50)

    text = Text(stt_wn, font=8, height=10, width=35)
    text.place(x=50, y=80)

    record_btn = Button(stt_wn, text='Record',font=("Candara", 16), bg='#fff68f', command=lambda: text.insert(END, record()))
    record_btn.place(x=220, y=330)

def instruction():
    instructions = '''
These are the instructions:
1. Wait for some time because STT and TTS conversions take time.
2. Pause for 2 seconds to end your phrase in STT conversion, because that is the pause_threshold amount.
'''
    showinfo("Instructions before beginning", instructions)

# Creating the main GUI window
root = Tk()
root.title("Speech & Text Converter")
#root.iconbitmap('icon.ico')
root.geometry('600x700')
root.resizable(0,0)

root.configure(background='#8ceacd')

img = Image.open('text-to-speech.png')

resized_img = img.resize((125,125))

img = ImageTk.PhotoImage(resized_img)

img_label=Label(root,image=img)
img_label.pack(pady=(50,10))
img_label.pack()

text_label = Label(root, text='SPEECH & TEXT CONVERTER',fg='#b21010',bg='#8ceacd')
text_label.pack()
text_label.config(font=("Candara", 28))

tts_btn = Button(root, text='Text-To-Speech Conversion', font=('Open Sans', 18), fg='#ffffff',bg='#A72B43', command=TTS)
tts_btn.place(x=135, y=260)

stt_btn = Button(root, text='Speech-To-Text Conversion', font=('Open Sans', 18), fg='#280d21',bg='#cceaea', command=STT)
stt_btn.place(x=135, y=360)

instruction_btn = Button(root, text='Instructions Before Starting', font=('Open Sans', 18), fg='#ffffff',bg='#05313d',
                        command=instruction)
instruction_btn.place(x=138, y=460)

root.update()
root.mainloop()