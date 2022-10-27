from video_translator import create_app
from os import environ
import os

root = os.path.realpath(os.path.join(os.path.dirname(__file__)))

app = create_app(root)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=environ.get("PORT", 5000),debug = True)