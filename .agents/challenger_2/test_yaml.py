import yaml
import re

# Extract docker-compose yaml from 04_Deployment_Diagram.md
with open(r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md", "r", encoding="utf-8") as f:
    content = f.read()

compose_match = re.search(r"```yaml\s*\n(version:.*?\n```)", content, re.DOTALL)
if compose_match:
    compose_str = compose_match.group(1).rstrip("`").strip()
    try:
        # Pre-replace bash-style parameter expansions for yaml parser validation
        cleaned_yaml = re.sub(r"\$\{[^}]+\}", "placeholder_val", compose_str)
        parsed = yaml.safe_load(cleaned_yaml)
        print("[PASS] docker-compose.prod.yml is valid YAML!")
        print(f"       Services found: {list(parsed.get('services', {}).keys())}")
        print(f"       Volumes found: {list(parsed.get('volumes', {}).keys())}")
        print(f"       Networks found: {list(parsed.get('networks', {}).keys())}")
    except Exception as e:
        print(f"[FAIL] docker-compose.prod.yml YAML Error: {e}")
else:
    print("[FAIL] docker-compose yaml block not found!")
