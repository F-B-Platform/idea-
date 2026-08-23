import re
import uuid

def validate_all_uuids():
    filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all strings that look like UUIDs
    uuid_pattern = re.compile(r"['\"]?([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})['\"]?")
    matches = uuid_pattern.findall(content)
    
    print(f"Total UUID occurrences found in file: {len(matches)}")
    unique_uuids = set(m.lower() for m in matches)
    print(f"Total unique UUIDs: {len(unique_uuids)}")

    invalid_uuids = []
    for u in unique_uuids:
        try:
            val = uuid.UUID(u)
        except Exception as ex:
            invalid_uuids.append((u, str(ex)))

    print(f"Invalid UUIDs: {len(invalid_uuids)}")
    for iu in invalid_uuids:
        print(f"  [INVALID UUID] {iu[0]}: {iu[1]}")

if __name__ == "__main__":
    validate_all_uuids()
