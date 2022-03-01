import pyttsx3
import sys
import multiprocessing
from TTS import Voice
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="DEBUG")


class VoiceAssistant():
    def __init__(self):
        logger.debug("Voice assistant is initiaized.")
        self.tts = Voice()
        voices = self.tts.get_voice_keys_for_language(language="")

    def run(self):
        logger.info("Starting the assistant...")
        self.tts.say("Hallo Sylwia, ich bin Tommy, deín Sprachassistent !")


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    voice_assistant = VoiceAssistant()
    voice_assistant.run()
