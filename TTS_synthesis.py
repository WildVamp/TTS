from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

path = "C:/Users/dhruv/anaconda3/envs/text-to-speech/Lib/site-packages/TTS/.models.json"

model_manager = ModelManager(path)

model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")

synth = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
)

text = "I love Chiku"
outputs = synth.tts(text)

synth.save_wav(outputs, "audio.wav")