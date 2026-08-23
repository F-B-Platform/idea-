import os
import re
import sys
import json

BASE_DIR = r"d:\Idea_DoAn"
TARGET_DIR = os.path.join(BASE_DIR, "05_Quy_Chuan_&_Test_Cases")

FILES = {
    "uat": os.path.join(TARGET_DIR, "UAT_Test_Cases.md"),
    "seed": os.path.join(TARGET_DIR, "Seed_Data_&_Database_Script.md"),
    "git": os.path.join(TARGET_DIR, "Git_Workflow_&_Branching_Strategy.md")
}

def analyze_file_lines_and_size():
    results = {}
    for key, path in FILES.items():
        if not os.path.exists(path):
            results[key] = {"exists": False}
            continue
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
            lines = content.splitlines()
        results[key] = {
            "exists": True,
            "path": path,
            "filename": os.path.basename(path),
            "size_bytes": os.path.getsize(path),
            "line_count": len(lines),
            "content": content,
            "lines": lines
        }
    return results

def search_patterns(files_data):
    # Prohibited placeholder patterns
    placeholder_regexes = [
        (r"\bTODO\b", "TODO"),
        (r"\bFIXME\b", "FIXME"),
        (r"\bTBD\b", "TBD"),
        (r"/\*\s*rest of", "/* rest of"),
        (r"//\s*rest of", "// rest of"),
        (r"//\s*tương tự", "// tương tự"),
        (r"//\s*giữ nguyên", "// giữ nguyên"),
        (r"\.\.\.", "... (ellipsis)"),
        (r"placeholder", "placeholder"),
    ]

    # Obsolete / purged terms
    purge_regexes = [
        (r"Staff Mobile App", "Staff Mobile App"),
        (r"Mobile App", "Mobile App"),
        (r"GPS\s*50m", "GPS 50m"),
        (r"30s\s*QR|QR\s*30s|QR\s*xoay\s*30s|xoay\s*30s", "30s QR / QR xoay 30s"),
        (r"\bC-23\b", "C-23"),
        (r"\bC-24\b", "C-24"),
    ]

    findings = {"placeholders": {}, "purged": {}}

    for key, data in files_data.items():
        if not data["exists"]:
            continue
        lines = data["lines"]
        findings["placeholders"][key] = []
        findings["purged"][key] = []

        for idx, line in enumerate(lines, 1):
            for regex_pat, name in placeholder_regexes:
                matches = re.finditer(regex_pat, line, re.IGNORECASE)
                for m in matches:
                    findings["placeholders"][key].append({
                        "pattern": name,
                        "line_num": idx,
                        "match_text": m.group(0),
                        "line_content": line.strip()
                    })

            for regex_pat, name in purge_regexes:
                matches = re.finditer(regex_pat, line, re.IGNORECASE)
                for m in matches:
                    findings["purged"][key].append({
                        "term": name,
                        "line_num": idx,
                        "match_text": m.group(0),
                        "line_content": line.strip()
                    })

    return findings

def audit_uat_details(uat_data):
    content = uat_data["content"]
    lines = uat_data["lines"]

    # Find test cases (e.g. TC-*)
    tc_headers = []
    tc_pattern = re.compile(r"^(?:#{2,4}\s+|\*\*)(TC-[A-Z0-9_\-]+)(?:\*\*|:|\s|\.|\b)", re.MULTILINE)
    # Also find any TC- in tables or headers
    all_tc_codes = set(re.findall(r"\b(TC-[A-Z0-9_\-]+)\b", content))
    
    # Specific targeted test cases
    expected_tcs = [
        "TC-DINE-01A", "TC-DINE-01B", "TC-DEL-01", "TC-TAKE-01",
        "TC-ATT-01", "TC-KDS-01", "TC-MGR-01", "TC-ADM-01"
    ]
    for i in range(1, 11):
        expected_tcs.append(f"TC-EDGE-{i:02d}")

    found_expected = {tc: (tc in all_tc_codes) for tc in expected_tcs}
    
    # Check 5-minute continuous Demo scenario
    demo_scenario = ("5 phút" in content or "5-Phút" in content or "5-phút" in content or "5-Minute" in content or "Demo" in content)
    
    return {
        "total_unique_tcs": len(all_tc_codes),
        "all_tc_codes": sorted(list(all_tc_codes)),
        "expected_check": found_expected,
        "demo_scenario_present": demo_scenario
    }

def audit_seed_details(seed_data):
    content = seed_data["content"]
    
    create_tables = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_\.\"]+)", content, re.IGNORECASE)
    insert_tables = re.findall(r"INSERT\s+INTO\s+([a-zA-Z0-9_\.\"]+)", content, re.IGNORECASE)
    
    unique_create_tables = sorted(list(set([t.replace('"', '').split('.')[-1] for t in create_tables])))
    unique_insert_tables = sorted(list(set([t.replace('"', '').split('.')[-1] for t in insert_tables])))
    
    expected_tables = [
        "branches", "roles", "users", "categories", "menu_items", "item_sizes",
        "ingredients", "recipes", "tables", "orders", "order_items",
        "payments", "shifts", "timekeepings", "inventory_checks", "inventory_check_details",
        "z_reports", "combo_suggestions"
    ]
    
    missing_creates = [t for t in expected_tables if not any(t in ct for ct in unique_create_tables)]
    missing_inserts = [t for t in expected_tables if not any(t in it for it in unique_insert_tables)]
    
    return {
        "total_create_tables": len(create_tables),
        "unique_create_tables": unique_create_tables,
        "total_insert_statements": len(insert_tables),
        "unique_insert_tables": unique_insert_tables,
        "missing_creates": missing_creates,
        "missing_inserts": missing_inserts
    }

def audit_git_details(git_data):
    content = git_data["content"]
    
    # Extract code blocks
    code_blocks = re.findall(r"```([a-zA-Z0-9_\-#+]*)\n(.*?)```", content, re.DOTALL)
    
    languages = {}
    for lang, code in code_blocks:
        lang = lang.lower() if lang else "unknown"
        languages[lang] = languages.get(lang, 0) + 1
        
    has_csharp = "csharp" in languages or "c#" in languages or "cs" in languages
    has_ts = "typescript" in languages or "ts" in languages or "tsx" in languages
    has_yaml = "yaml" in languages or "yml" in languages
    
    # Check for Clean Architecture, CQRS, MediatR, FluentValidation, Next.js App Router, Zod
    keywords = {
        "Clean Architecture / CQRS": bool(re.search(r"IRequest|IRequestHandler|MediatR|Command|Query", content)),
        "FluentValidation": bool(re.search(r"AbstractValidator|RuleFor", content)),
        "Result Pattern / Exceptions": bool(re.search(r"Result<|DomainException|GlobalExceptionHandler|Middleware", content)),
        "Next.js App Router / React": bool(re.search(r"use client|use server|async function|React|NextResponse", content)),
        "Zod Schema": bool(re.search(r"z\.object|z\.string|z\.infer", content)),
        "GitFlow Definitions": bool(re.search(r"feature/|release/|hotfix/|develop|main", content)),
        "Conventional Commits": bool(re.search(r"feat:|fix:|refactor:|docs:|test:|chore:", content)),
        "SonarQube / CI/CD Gates": bool(re.search(r"sonar|github/workflows|\.github|actions", content, re.IGNORECASE))
    }
    
    return {
        "code_blocks_count": len(code_blocks),
        "languages": languages,
        "keyword_checks": keywords
    }

def audit_callouts(files_data):
    callouts = {}
    callout_pattern = re.compile(r">\s*\[!(NOTE|IMPORTANT|TIP|WARNING|CAUTION)\]", re.IGNORECASE)
    for key, data in files_data.items():
        if not data["exists"]:
            continue
        matches = callout_pattern.findall(data["content"])
        callouts[key] = {
            "total": len(matches),
            "breakdown": {}
        }
        for m in matches:
            t = m.upper()
            callouts[key]["breakdown"][t] = callouts[key]["breakdown"].get(t, 0) + 1
    return callouts

def main():
    files_data = analyze_file_lines_and_size()
    patterns_findings = search_patterns(files_data)
    uat_audit = audit_uat_details(files_data["uat"])
    seed_audit = audit_seed_details(files_data["seed"])
    git_audit = audit_git_details(files_data["git"])
    callout_audit = audit_callouts(files_data)
    
    report = {
        "files_stats": {
            k: {
                "exists": v["exists"],
                "filename": v.get("filename"),
                "size_bytes": v.get("size_bytes"),
                "line_count": v.get("line_count")
            } for k, v in files_data.items()
        },
        "patterns_findings": patterns_findings,
        "uat_audit": uat_audit,
        "seed_audit": seed_audit,
        "git_audit": git_audit,
        "callout_audit": callout_audit
    }
    
    out_json = os.path.join(BASE_DIR, ".agents", "auditor_zero_placeholder", "audit_data.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        
    print("AUDIT EXECUTION COMPLETE. Summary:")
    for k, v in report["files_stats"].items():
        print(f"File {v['filename']}: {v['line_count']} lines, {v['size_bytes']} bytes")
    print(f"UAT Test Cases Found: {report['uat_audit']['total_unique_tcs']}")
    print(f"Seed CREATE TABLE count: {report['seed_audit']['total_create_tables']}, Unique: {len(report['seed_audit']['unique_create_tables'])}")
    print(f"Seed INSERT statement count: {report['seed_audit']['total_insert_statements']}, Unique: {len(report['seed_audit']['unique_insert_tables'])}")
    print(f"Git Code blocks count: {report['git_audit']['code_blocks_count']}")
    print("Placeholder findings count:", {k: len(v) for k, v in patterns_findings["placeholders"].items()})
    print("Purged terms findings count:", {k: len(v) for k, v in patterns_findings["purged"].items()})

if __name__ == "__main__":
    main()
