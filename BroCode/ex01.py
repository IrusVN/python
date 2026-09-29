# Bài tập 1: Kiểm tra tính hợp lệ của file ảnh (Input &amp; If/Else)

# * **Yêu cầu:** Viết chương trình yêu cầu người dùng nhập tên file (ví dụ: `image01.jpg`) và dung lượng file tính bằng MB (ví dụ: `4.5`).
# * **Đăng ký điều kiện:**
#   * File hợp lệ nếu tên file kết thúc bằng `.jpg` hoặc `.png` và dung lượng nhỏ hơn hoặc bằng 10 MB.
#   * Nếu không thỏa mãn, in ra lý do cụ thể (sai định dạng file hay dung lượng quá lớn).

name_file = input("Enter name file (only .jpg or .png): ")

if (name_file.endswith(".jpg") or name_file.endswith(".png")):
    size_file = float(input("Enter size file(MB): "))
    if size_file <= 10 and size_file > 0:
        print(f"File {name_file} is valid")
    else:
        print(f"File {name_file} must be less than or equal to 10MB")
else:
    print(f"File {name_file} is invalid")
