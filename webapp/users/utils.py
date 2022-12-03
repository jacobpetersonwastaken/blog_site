import secrets
import os
from PIL import Image
from flask import current_app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_file_name = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images', picture_file_name)
    print(f_ext, type(f_ext))
    if f_ext != '.svg':
        output_size = (125, 125)
        i = Image.open(form_picture)
        i.thumbnail(output_size)
        i.save(picture_path)
    else:
        form_picture.save(picture_path)
    return picture_file_name
