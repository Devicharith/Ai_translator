import subprocess

def add_subs(video,subs_video):
    subprocess.run(["ffmpeg","-i",video,"-vf","subtitles=trans_sub.vtt",subs_video+".mp4"])
