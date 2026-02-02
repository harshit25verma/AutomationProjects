import os
import shutil

DOWNLOADS = "Downloads"

EXTENSIONS = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Docs": [".pdf", ".docx"],
    "Code": [".py", ".js"]
}

for file in os.listdir(DOWNLOADS):
    for folder, exts in EXTENSIONS.items():
        if file.endswith(tuple(exts)):
            os.makedirs(folder, exist_ok=True)
            shutil.move(
                os.path.join(DOWNLOADS, file),
                os.path.join(folder, file)
            )