#### **Bài tập 1: Tự động chuẩn hóa tên file dataset (String Methods &amp; Slicing)**

# * **Yêu cầu:**
#   * Cho người dùng nhập vào một tên file ảnh bất kỳ từ bàn phím (ví dụ: `" Hero_Character_01.JPG "` hoặc `"bad_file.txt"`).
#   * Sử dụng các hàm xử lý chuỗi để:
#     1. Xóa khoảng trắng thừa ở 2 đầu chuỗi (`.strip()`).
#     2. Chuyển toàn bộ tên file về chữ thường (`.lower()`).
#     3. Tách lấy **tên file** và **phần mở rộng (extension)** bằng Slicing hoặc `.rfind(".")`.
#     4. Nếu phần mở rộng là `.jpg` hoặc `.png`, in ra tên file đã được làm sạch theo chuẩn: `[CLEANED] hero_character_01.jpg`.
#     5. Nếu không đúng định dạng ảnh, in ra thông báo lỗi.

name_file = input("Enter file name (q to quit): ")
while name_file.strip().lower() != "q":
    cleaned_name = name_file.strip().lower()
    dot_index = cleaned_name.rfind(".")
    if dot_index != -1:
        file_name = cleaned_name[:dot_index]
        extentions = cleaned_name[dot_index:]

        if file_name == "":
            print("Error: File name cannot be empty.")
        elif extentions in [".jpg", ".png"]:
            print(f"[CLEANED] {file_name}{extentions}")
        else:
            print(f"Error: Invalid file extension '{extentions}'. Only .jpg and .png are allowed.")
    else:
        print("Error: No file extension found.")
    name_file = input("Enter file name (q to quit): ")
