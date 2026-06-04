# backend/app/services/audio_service.py
from pydub import AudioSegment
import os

from app.services.youtube_service import download_youtube_audio


def convert_to_wav(input_path: str):

    output_path = os.path.splitext(input_path)[0] + "_converted.wav"

    audio = AudioSegment.from_file(input_path)

    audio = audio.set_channels(1).set_frame_rate(16000)

    audio.export(output_path, format="wav")

    return output_path


def chunk_audio(wav_path: str, chunk_minutes: int = 10):

    audio = AudioSegment.from_wav(wav_path)

    chunk_ms = chunk_minutes * 60 * 1000

    chunks = []

    for i, start in enumerate(range(0, len(audio), chunk_ms)):

        chunk = audio[start:start + chunk_ms]

        chunk_path = f"{wav_path}_chunk_{i}.wav"

        chunk.export(chunk_path, format="wav")

        chunks.append(chunk_path)

    return chunks


def process_input(source: str):

    if source.startswith("http"):

        wav_path = download_youtube_audio(source)

    else:

        wav_path = convert_to_wav(source)

    return chunk_audio(wav_path)