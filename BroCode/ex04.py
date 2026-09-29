#### **Bài tập 2: Giả lập vòng lặp quét khung hình Video (For Loop &amp; Format Specifier)**

# * **Yêu cầu:**
#   * Viết một vòng lặp `for` duyệt qua 5 khung hình (tương ứng từ frame `1` đến `5`).
#   * Ở mỗi frame, giả định thời gian xử lý AI (processing time) tăng dần theo công thức: `processing_time = frame * 0.01234`.
#   * In ra báo cáo dạng bảng được định dạng đẹp mắt như sau:
#     * Frame phải có 3 chữ số (ví dụ: `001`, `002`, `003`).
#     * Thời gian xử lý làm tròn lấy **3 chữ số thập phân** kèm đơn vị `s`.
#     * *Kết quả mong muốn:*

# ```
# Frame 001 | Processing time: 0.012s | Status: OK
# Frame 002 | Processing time: 0.025s | Status: OK
# Frame 003 | Processing time: 0.037s | Status: OK
# ```

for frame in range(1, 6):
    processing_time = frame * 0.01234
    print(f"Frame {frame:03d} | Processing time: {processing_time:.3f}s | Status: OK")
