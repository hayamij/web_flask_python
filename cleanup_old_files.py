# Script để dọn dẹp các files cũ không cần thiết
# Run: python cleanup_old_files.py

import os
import shutil

print("🧹 Bắt đầu dọn dẹp files cũ không sử dụng...\n")

# Files và folders cần xóa
items_to_remove = [
    "app.py",  # Đã thay bằng run.py
    "templates",  # Đã move vào app/templates
    "static",  # Đã move vào app/static
]

removed = []
not_found = []

for item in items_to_remove:
    if os.path.exists(item):
        try:
            if os.path.isfile(item):
                os.remove(item)
                removed.append(f"✅ Đã xóa file: {item}")
            elif os.path.isdir(item):
                shutil.rmtree(item)
                removed.append(f"✅ Đã xóa folder: {item}")
        except Exception as e:
            print(f"❌ Lỗi khi xóa {item}: {str(e)}")
    else:
        not_found.append(f"⚠️  Không tìm thấy: {item}")

print("\n📋 KẾT QUẢ:\n")
for msg in removed:
    print(msg)

if not_found:
    print("\n")
    for msg in not_found:
        print(msg)

print("\n✅ Hoàn tất! Dự án đã sạch sẽ và tuân thủ cấu trúc mới.")
print("👉 Chạy: python run.py để khởi động server\n")
