from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
from filters import adjust_brightness, blur_background, cartoon_filter, oil_paint_effect
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Lấy file tải lên
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # Áp dụng bộ lọc
            filter_type = request.form['filter']
            image = cv2.imread(filepath)

            if filter_type == 'brightness':
                result = adjust_brightness(image)
            elif filter_type == 'blur':
                result = blur_background(image)
            elif filter_type == 'cartoon':
                result = cartoon_filter(image)
            elif filter_type == 'oil_paint':
                result = oil_paint_effect(image)
            else:
                result = image

            # Lưu ảnh đã chỉnh sửa
            result_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg')
            cv2.imwrite(result_path, result)
            return render_template("index.html", uploaded_image=file.filename, result_image='result.jpg')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
