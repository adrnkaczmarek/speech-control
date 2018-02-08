import logging
from flask import Flask, request
from gpio_controller import GPIOController
import speech_recognition as sr
import RPi.GPIO as GPIO


def init_logger():
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logger.setLevel(logging.INFO)
    open('example.log', 'w+')
    handler = logging.FileHandler('example.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


log = init_logger()
pwmController = GPIOController()

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
freq = 1

pwm = GPIO.PWM(12, freq)
pwm.start(50.0)



@app.route('/api/sound', methods=['POST'])
def change_frequency():
    GPIO.cleanup()
    r = sr.Recognizer()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    freq = 1

    pwm = GPIO.PWM(12, freq)
    pwm.start(50.0)
    if request.method == 'POST':
        wav = request.files['test.wav']

        with sr.WavFile(wav) as source:
            audio = r.record(source)
        try:
            spoken_audio = r.recognize_google(audio)


            if spoken_audio == "turn off":
                pwm.ChangeDutyCycle(0.0)
                print(spoken_audio)
            if spoken_audio == "turn on":
                pwm.ChangeDutyCycle(100.0)
                print(spoken_audio)
            if spoken_audio == "slower":
                if freq >= 3:
                    pwm.start(50.0)
                    pwm.ChangeFrequency(freq)
                    freq -= 3
                print(spoken_audio)
            if spoken_audio == "faster":
                pwm.start(50.0)
                freq += 3
                pwm.ChangeFrequency(freq)
                print(spoken_audio)

        except LookupError:
            print("Google Speech Recognition could not understand audio")

    print("test-succesful")
    return 'file uploaded successfully'


@app.route('/api/test', methods=['GET'])
def test():
    print("test-succesful")
    return 'test_succesful'


if __name__ == '__main__':
    log.info("Flask started.")
    app.run(host='0.0.0.0', port=5020)