import os
import subprocess
from config.definitions import ROOT_DIR

def run(path):
    file = ROOT_DIR+r"/vosk-api-master/python/example/test_webvtt.py"
    subprocess.run(["python",file,path,"subs.vtt"])