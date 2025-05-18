from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(mp4_path, mp3_path):
    """
    mp4ファイルをmp3ファイルに変換する関数

    Args:
        mp4_path (str): 変換元のmp4ファイルのパス
        mp3_path (str): 変換先のmp3ファイルのパス
    """
    try:
        video_clip = VideoFileClip(mp4_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_path)
        audio_clip.close()
        video_clip.close()
        print(f"{mp4_path} を {mp3_path} に変換しました。")
    except Exception as e:
        print(f"変換中にエラーが発生しました: {e}")

if __name__ == "__main__":
    # フォルダなかったら作成
    import os
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    # 変換するmp4ファイルのパス
    mp4_filename = "sample.mp4"
    mp4_path = f"src/data/{mp4_filename}"
    # 拡張子抜いたパス
    mp4_filename_withoutEx = mp4_filename.split(".")[0]
    # 出力するmp3ファイルのパス
    mp3_path = f"outputs/{mp4_filename_withoutEx}.mp3"

    # mp4をmp3に変換
    convert_mp4_to_mp3(mp4_path, mp3_path)