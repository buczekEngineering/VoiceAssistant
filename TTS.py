from loguru import logger
import time
import pyttsx3
import multiprocessing


def __speak__(text, voice_id):
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()


class Voice:

    def __init__(self):
        self.process = None
        self.voice_id = "1"

    def say(self, text):
        if self.process:
            self.stop()
        p = multiprocessing.Process(target=__speak__, args=(text, self.voice_id))
        p.start()
        self.process = p

    def set_voice(self, voice_id):
        self.voice_id = voice_id

    def stop(self):
        if self.process:
            self.process.terminate()

    def get_voice_keys_for_language(self, language=""):
        result = list()
        engine = pyttsx3.init()
        lang_search_string = language.upper() + "_"
        logger.info(f"LANGUAGE SEARCH STRING: {lang_search_string}")
        voices = engine.getProperty('voices')
        for voice in voices:
            if language == "":
                result.append(voice.id)
            elif lang_search_string in voice.id:
                logger.info("VOICE FOUND!")
                result.append(voice.id)
        return result
