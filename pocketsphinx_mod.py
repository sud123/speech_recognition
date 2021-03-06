from pocketsphinx import LiveSpeech
import speech_recognition as sr


def listen_pocketsphinx():
    for phrase in LiveSpeech():
        print("Listening!")
        res = str(phrase)
        print(res)
        if res.__contains__("book meeting"):
            print("meeting booked")
            break


def listen_sr():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # listen for 5 seconds and create the ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=5)
        print("Say something!")
        audio = r.listen(source)

        # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said '" + r.recognize_google(audio) + "'")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


if __name__=="__main__":
    listen_sr()