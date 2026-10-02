# #### **Bài tập 1: Quản lý nhãn Bounding Box vật thể bằng Dictionary**

# * **Yêu cầu:**
#   1. Tạo một dictionary đặt tên là `image_info` chứa các thông tin ban đầu:
#     * `"filename"`: `"character_01.jpg"`
#     * `"label"`: `"hero"`
#     * `"bbox"`: `[100, 150, 300, 400]` *(tọa độ khung nhận diện [xmin, ymin, xmax, ymax])*
#     * `"confidence"`: `0.85` *(độ tin cậy của mô hình)*
#   2. Dùng hàm `.get()` để lấy ra giá trị của `"confidence"`. Nếu `confidence &lt; 0.9`, hãy cập nhật (update) trường `"status"` thành `"need_review"`, ngược lại cập nhật thành `"approved"`.
#   3. Thêm trường `"resolution"` có giá trị là tuple `(1920, 1080)` vào dictionary bằng phương thức `.update()`.
#   4. Dùng vòng lặp `for key, value in image_info.items():` để in ra toàn bộ thông tin của bức ảnh theo định dạng: `Key: Value`.

image_info = {
    "filename": "character_01.jpg",
    "label": "hero",
    "bbox": [100, 150, 300, 400],
    "confidence": 0.85
}

if float(image_info.get("confidence")) < 0.9:
    image_info["status"] = "need_review"
else:
    image_info["status"] = "approved"

image_info.update({"resolution": (1920, 1080)})

for key, value in image_info.items():
    print(f"{key}: {value}")
