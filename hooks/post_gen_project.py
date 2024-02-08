import os
import shutil

REMOVE_PATHS = [
   '{{cookiecutter.project_slug}}/{{cookiecutter.filename}}.txt'
]

for path in REMOVE_PATHS:
    if os.path.exists(path):
        shutil.rmtree(path)
