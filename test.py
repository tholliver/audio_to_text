# from re import T
# from vosk import Model, KaldiRecognizer
# import pyaudio

# model = Model('./es-lite')
# recog = KaldiRecognizer(model, 16000)

# cap = pyaudio.PyAudio()
# stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
#                   frames_per_buffer=8192)
# stream.start_stream()

# while(True):
#     data = stream.read(4096)
#     # if len(data) == 0:
#     #     break
#     if recog.AcceptWaveform(data):
#         print(f'Boom: {recog.Result()}')


import json
import wave

from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import os


def mp3_to_wav(source, skip=0, excerpt=False):

    sound = AudioSegment.from_mp3(source)  # load source
    sound = sound.set_channels(1)  # mono
    sound = sound.set_frame_rate(16000)  # 16000Hz

    if excerpt:
        # 30 seconds - Does not work anymore when using skip
        excrept = sound[skip*500:skip*2000+20000]
        output_path = os.path.splitext(source)[0]+"_excerpt.wav"
        excrept.export(output_path, format="wav")
    else:
        audio = sound[skip*1000:]
        output_path = os.path.splitext(source)[0]+".wav"
        audio.export(output_path, format="wav")

    return output_path


def transcript_file(input_file, model_path):

    # Check if file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(os.path.basename(input_file) + " not found")

    # Check if model path exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(os.path.basename(model_path) + " not found")

    # open audio file
    wf = wave.open(input_file, "rb")
    print(f'Here::::: {wf}')

    # check if wave file has the right properties
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise TypeError("Audio file must be WAV format mono PCM.")

    # Initialize model
    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())

    # Get file size (to calculate progress bar)
    file_size = os.path.getsize(input_file)

    # Run transcription

    # To store our results
    transcription = []

    while True:
        data = wf.readframes(4000)  # use buffer of 4000

        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # Convert json output to dict
            result_dict = json.loads(rec.Result())
            # Extract text values and append them to transcription list
            transcription.append(result_dict.get("text", ""))

    # Get final bits of audio and flush the pipeline
    final_result = json.loads(rec.FinalResult())
    transcription.append(final_result.get("text", ""))

    transcription_text = ' '.join(transcription)

    return transcription_text


# please specify here the path to your mp3 file
wave_file = mp3_to_wav('./audios/chon.mp3', 37, True)
waveFile = './audios/boo.wav'
transcription = transcript_file(wave_file, './es')
print(transcription)
