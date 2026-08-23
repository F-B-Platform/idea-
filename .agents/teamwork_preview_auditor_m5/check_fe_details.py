import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== CHECKING FILE 06_Quy_Trinh_Frontend.md ===")

# Check 5 Zustand Stores
stores = [
    "useCartStore",
    "usePosStore",
    "useKdsStore",
    "useShiftStore",
    "useAuthStore"
]
print("Zustand Stores Verification:")
for s in stores:
    found = s in content
    print(f"  {s}: {'PASS' if found else 'FAIL'}")

# Check Web Audio API Chime
audio_api = bool(re.search(r"AudioContext|Web\s+Audio\s+API|playChime|chime", content, re.IGNORECASE))
print(f"Web Audio API Chime present: {audio_api}")

# Check Service Worker offline cache
sw_cache = bool(re.search(r"service\s*worker|sw\.js|CacheStorage|caches\.open", content, re.IGNORECASE))
print(f"Service Worker offline menu cache present: {sw_cache}")

# Check TanStack Query
tanstack = bool(re.search(r"TanStack|useQuery|useMutation", content))
print(f"TanStack Query present: {tanstack}")
