import moviepy.editor
from pathlib import Path

#��� ���������� ����� mp4 � mp3 � ��� �� ���������, ���������� ���������� Path
video_file = Path('sample.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')

