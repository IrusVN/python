# #### **Bài tập 2: Lọc ảnh trùng &amp; Phân chia Dataset Train/Val (Set, List &amp;** **random** **)**

# * **Yêu cầu:**
#   1. Cho danh sách file ảnh bị trùng lặp ban đầu: `raw_images = ["img01.jpg", "img02.jpg", "img01.jpg", "img03.jpg", "img04.jpg", "img02.jpg", "img05.jpg", "img06.jpg", "img07.jpg", "img08.jpg", "img09.jpg", "img10.jpg"]`
#   2. Sử dụng `set()` để loại bỏ toàn bộ file trùng lặp, sau đó chuyển ngược lại thành `list` và sắp xếp theo thứ tự.
#   3. Xáo trộn danh sách ảnh này một cách ngẫu nhiên bằng `random.shuffle()`.
#   4. Tính toán để chia danh sách làm 2 phần:
#     * **Train set:** Lấy 80% số lượng ảnh đầu tiên.
#     * **Validation set:** Lấy 20% số lượng ảnh còn lại.
#   5. In ra số lượng ảnh và danh sách ảnh của từng tập (`Train` và `Val`).

import random

raw_images = ["img01.jpg", "img02.jpg", "img01.jpg", "img03.jpg", "img04.jpg", "img02.jpg", "img05.jpg", "img06.jpg", "img07.jpg", "img08.jpg", "img09.jpg", "img10.jpg"]

cleaned_images = list(set(raw_images))
cleaned_images.sort()

random.shuffle(cleaned_images)

train_size = int(len(cleaned_images) * 0.8)
train_set = cleaned_images[:train_size]
val_set = cleaned_images[train_size:]

print(f"Train set ({len(train_set)} images): {train_set}")
print(f"Validation set ({len(val_set)} images): {val_set}")
