import pyttsx3
import yaml
import sys
import multiprocessing
from TTS import Voice
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="DEBUG")

CONFIG_FILE = 'config.yml'


class VoiceAssistant():
    def __init__(self):

        global CONFIG_FILE
        with open(CONFIG_FILE, "r", encoding="utf-8")as yamlfile:
            self.cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)
            print(self.cfg)
        if self.cfg:
            logger.debug("Config file found and applied.")
        else:
            logger.error("No config file found.")

        language = self.cfg["assistant"]["language"]
        if not language:
            language = "de"
        logger.info(f"Used language: {language}")
        logger.debug("Voice assistant is initiaized.")
        self.tts = Voice()
        voice = self.tts.get_voice_keys_for_language(language=language)
        logger.info(f"Choosed voice: {voice}")
        if len(voice) > 0:
            self.tts.set_voice(voice[0])

    def run(self):
        logger.info("Starting the assistant...")
        self.tts.say("Hallo Sylwia, ich bin Tommy, deín Sprachassistent!")


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    voice_assistant = VoiceAssistant()
    voice_assistant.run()
