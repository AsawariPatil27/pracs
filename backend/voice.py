from sarvamai import SarvamAI
from dotenv import load_dotenv
import os

load_dotenv()

API_SUBSCRIBTION_KEY = os.getenv("SARVAM_API_KEY")
_client = SarvamAI(api_subscription_key=API_SUBSCRIBTION_KEY)


def voice_to_text(audio_path):
    with open(audio_path, "rb") as f:
        response = _client.speech_to_text.transcribe(
            file=f,
            model="saaras:v3",
            language_code="en-IN",
            mode="transcribe",
        )

    text = response.transcript or ""
    detected = getattr(response, "language_code", "unknown")

    return {
        "text": text,
        "detectedLanguage": detected,
        "languageProbability": 1.0,
    }
