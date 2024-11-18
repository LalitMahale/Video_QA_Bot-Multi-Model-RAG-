import os
from pathlib import Path


filelist = [
    "experiments/experiments.ipynb",
    "src/__init__.py",
    "src/config.py",
    "src/prompt.py",
    "src/processing.py",
    "src/pipeline.py",
    "src/hf_pipeline.py",
    "processed_data/video/.gitkeep",
    "processed_data/images/.gitkeep",
    "processed_data/transcription_document/.gitkeep",
    "logs/video_qa_bot.log",
    "app.py",
    ".gitignore",
    ".dockerignore",
    "Dockerfile",
    ".env",
    "requirements.txt"
]


for file in filelist:
    file = Path(file)
    folder,filename = os.path.split(file)
    
    if folder != "":

        os.makedirs(folder,exist_ok=True)
    
    if (not os.path.exists(folder)) or (os.path.getsize(folder)==0):
        with open(file,"w") as f:
            pass

