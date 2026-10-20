# #### **Bài tập 2: Ghi Log Metadata đa dạng với** **\*args** **và** **\*\*kwargs**

# * **Yêu cầu:**
#   1. Viết hàm `log_image_annotation(image_name, *tags, **metadata)` có nhiệm vụ in báo cáo gán nhãn cho 1 bức ảnh:
#     * `image_name`: Tên file ảnh (tham số bắt buộc).
#     * `*tags`: Nhận số lượng nhãn vật thể xuất hiện trong ảnh tùy ý (ví dụ: `"hero"`, `"tree"`, `"monster"`).
#     * `**metadata`: Nhận thêm các thông tin phụ trợ tùy ý dạng `key=value` (ví dụ: `width=1920`, `height=1080`, `status="approved"`).
#   2. Hàm sẽ in ra báo cáo dạng:

# ```
# === ANNOTATION LOG: character_01.jpg ===
# Tags detected: ['hero', 'weapon']
# Additional Metadata:
#   - width: 1920
#   - height: 1080
#   - status: approved

# ```

# * Thử gọi hàm với ít nhất 2 bức ảnh có số lượng tags và metadata khác nhau.

def log_image_annotation(image_name, *tags, **metadata):
    print("=== ANNOTATION LOG: {} ===".format(image_name))
    print("Tags detected:", list(tags))
    if metadata:
        print("Additional Metadata:")
        for key, value in metadata.items():
            print(f"  - {key}: {value}")

log_image_annotation("character_01.jpg", "hero", "weapon", width=1920, height=1080, status="approved")
log_image_annotation("background_01.png", "tree", "monster", width=1280, height=720, status="pending", author="John Doe")