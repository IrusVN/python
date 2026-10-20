# #### **Bài tập 1: Lọc &amp; Làm sạch Dataset bằng List Comprehension &amp; Function**

# * **Yêu cầu:**
#   1. Viết một hàm tên là `clean_filepaths(raw_paths)` nhận vào một danh sách các đường dẫn file thô.
#   2. Bên trong hàm, sử dụng **List Comprehension** (chỉ viết trên 1 dòng) để:
#     * Cắt bỏ khoảng trắng thừa ở 2 đầu từng tên file (`.strip()`).
#     * Chuyển về chữ thường (`.lower()`).
#     * Chỉ giữ lại các file có đuôi hợp lệ là `.jpg` hoặc `.png`.
#   3. Mẫu dữ liệu đầu vào để test: `raw_data = [" hero.PNG ", "monster.JPG", "background.bmp", " EFFECT.png ", "notes.txt"]`
#   4. Gọi hàm và in kết quả ra màn hình.

# ####

def clean_filepaths(raw_paths):
    return [path.strip().lower() for path in raw_paths if path.strip().lower().endswith((".jpg", ".png"))]

raw_data = [" hero.PNG ", "monster.JPG", "background.bmp", " EFFECT.png ", "notes.txt"]
print(clean_filepaths(raw_data))
