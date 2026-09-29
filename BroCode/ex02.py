# #### **Bài tập 2: Phân loại độ phân giải khung hình (Math &amp; If/Elif/Else)**

# * **Yêu cầu:** Nhập chiều rộng (`width`) và chiều cao (`height`) của một bức ảnh từ bàn phím (đơn vị pixel).
# * **Đăng ký điều kiện:**
#   * Tính tổng số điểm ảnh `total_pixels = width * height`.
#   * Nếu `total_pixels &gt;= 2,073,600` (tương đương Full HD 1920x1080): In ra `"Ảnh chất lượng cao (Full HD+)"`.
#   * Nếu `total_pixels &gt;= 921,600` (tương đương HD 1280x720): In ra `"Ảnh chất lượng trung bình (HD)"`.
#   * Còn lại: In ra `"Ảnh chất lượng thấp (Cần lọc bỏ)"`.

width = int(input("Enter width: "))
if width > 0:
    height = int(input("Enter height: "))
    if height > 0:
        total_pixels = width * height
        if total_pixels >= 2_073_600:
            print("Image quality is high (Full HD+)")
        elif total_pixels >= 921_600:
            print("Image quality is medium (HD)")
        else:
            print("Image quality is low (Need to filter out)")
    else:
        print("The height must be greater than 0.")
else:
    print("The width must be greater than 0.")
