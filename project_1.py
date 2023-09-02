import moviepy.editor
from pathlib import Path

#для сохранения файла mp4 в mp3 с тем же названием, используем библиотеку Path
video_file = Path('sample.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')

