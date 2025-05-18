from faster_whisper import WhisperModel

model = WhisperModel(
    model_size_or_path="deepdml/faster-whisper-large-v3-turbo-ct2",
    device="cuda",
    compute_type="int8"
)

segments, info = model.transcribe(
    "DougaKirinukiTool/data/sample.wav",
    vad_filter=False,
    beam_size=5
)
for seg in segments:
    print(f"[{seg.start:.2f} - {seg.end:.2f}] {seg.text}")
print("処理終了！")