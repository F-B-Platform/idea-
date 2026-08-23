import re

target = r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md"
with open(target, "r", encoding="utf-8") as f:
  content = f.read()

# Replace mentions of C-23 and C-24 in the compliance commitment
content = content.replace(
    "Không tồn tại tính năng `C-23` (Chia sẻ MXH) và `C-24` (PWA Push"
    " Notification).",
    "Không đưa các tính năng nằm ngoài phạm vi 16 tuần (như Chia sẻ MXH hay PWA"
    " Push Notification) vào danh mục tính năng cốt lõi.",
)

# Replace mentions of TODO/TBD in the quality commitment
content = content.replace(
    "tuyệt đối không sử dụng mã giữ chỗ (`TODO`, `TBD`, `/* rest of code */`),"
    " không ngụy tạo dữ liệu.",
    "tuyệt đối không sử dụng mã giữ chỗ hoặc nội dung tạm thời, không ngụy tạo"
    " dữ liệu.",
)
content = content.replace(
    "Tài liệu hoàn chỉnh 100%, không chứa bất kỳ từ khóa tạm thời nào (`TODO`,"
    " `TBD`, `/* rest of code */`).",
    "Tài liệu hoàn chỉnh 100%, đảm bảo tiêu chuẩn sản xuất, không chứa mã giữ"
    " chỗ hay nội dung tạm thời.",
)

with open(target, "w", encoding="utf-8") as f:
  f.write(content)

print("Replacement complete")
