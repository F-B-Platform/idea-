import os
import re
import sys
import subprocess
import shutil

sys.stdout.reconfigure(encoding='utf-8')

FILE_PATH = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md"

def extract_ts_files():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    code_blocks = re.findall(r'```([a-zA-Z0-9_-]*)\r?\n(.*?)```', content, re.DOTALL)
    ts_blocks = [(lang, code) for lang, code in code_blocks if lang.lower() in ('tsx', 'typescript')]
    
    files = {}
    for lang, code in ts_blocks:
        m = re.search(r'//\s*File:\s*(.*?)\r?\n', code)
        if m:
            file_rel_path = m.group(1).strip()
            files[file_rel_path] = (lang, code)
        else:
            print(f"Warning: no // File: header in {lang} block!")
            
    return files

def setup_and_typecheck_ts():
    test_dir = r"d:\Idea_DoAn\tests\ts_verification"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir, ignore_errors=True)
    os.makedirs(test_dir, exist_ok=True)
    
    # Create package.json
    package_json = """{
  "name": "smartfb-ts-test",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "@microsoft/signalr": "^8.0.7",
    "clsx": "^2.1.1",
    "lucide-react": "^0.439.0",
    "next": "^14.2.10",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "tailwind-merge": "^2.5.2",
    "zustand": "^4.5.5"
  },
  "devDependencies": {
    "@types/node": "^20.16.5",
    "@types/react": "^18.3.5",
    "@types/react-dom": "^18.3.0",
    "typescript": "^5.5.4"
  }
}
"""
    with open(os.path.join(test_dir, "package.json"), "w", encoding="utf-8") as f:
        f.write(package_json)
        
    # Create tsconfig.json
    tsconfig_json = """{
  "compilerOptions": {
    "target": "es2020",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
"""
    with open(os.path.join(test_dir, "tsconfig.json"), "w", encoding="utf-8") as f:
        f.write(tsconfig_json)

    with open(os.path.join(test_dir, "next-env.d.ts"), "w", encoding="utf-8") as f:
        f.write('/// <reference types="next" />\n/// <reference types="next/image-types/global" />\n')

    # Write extracted TS files
    extracted_files = extract_ts_files()
    for rel_path, (lang, code) in extracted_files.items():
        dest_path = os.path.join(test_dir, rel_path.replace("/", os.sep))
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Wrote extracted file: {rel_path}")

    # Write shadcn / helper component stubs and lib/utils.ts
    os.makedirs(os.path.join(test_dir, "src", "lib"), exist_ok=True)
    with open(os.path.join(test_dir, "src", "lib", "utils.ts"), "w", encoding="utf-8") as f:
        f.write("""import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
""")

    # Write UI component stubs for ModifierDrawer
    os.makedirs(os.path.join(test_dir, "src", "components", "ui"), exist_ok=True)
    with open(os.path.join(test_dir, "src", "components", "ui", "drawer.tsx"), "w", encoding="utf-8") as f:
        f.write("""import * as React from "react";
export const Drawer = ({ children, open, onOpenChange }: any) => <div data-open={open}>{children}</div>;
export const DrawerContent = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerHeader = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerTitle = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerDescription = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerFooter = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerClose = ({ children, asChild }: any) => <div>{children}</div>;
""")

    with open(os.path.join(test_dir, "src", "components", "ui", "button.tsx"), "w", encoding="utf-8") as f:
        f.write("""import * as React from "react";
export const Button = React.forwardRef<HTMLButtonElement, any>(({ className, variant, size, children, ...props }, ref) => (
  <button ref={ref} className={className} {...props}>{children}</button>
));
""")

    with open(os.path.join(test_dir, "src", "components", "ui", "badge.tsx"), "w", encoding="utf-8") as f:
        f.write("""import * as React from "react";
export const Badge = ({ className, variant, children }: any) => <span className={className}>{children}</span>;
""")

    with open(os.path.join(test_dir, "src", "components", "ui", "scroll-area.tsx"), "w", encoding="utf-8") as f:
        f.write("""import * as React from "react";
export const ScrollArea = ({ className, children }: any) => <div className={className}>{children}</div>;
""")

    # Write customer component stubs for TableOrderPage
    os.makedirs(os.path.join(test_dir, "src", "components", "customer"), exist_ok=True)
    with open(os.path.join(test_dir, "src", "components", "customer", "TableHeaderBanner.tsx"), "w", encoding="utf-8") as f:
        f.write("""import React from "react";
export const TableHeaderBanner = (props: any) => <div {...props} />;
""")
    with open(os.path.join(test_dir, "src", "components", "customer", "CategoryNavTabs.tsx"), "w", encoding="utf-8") as f:
        f.write("""import React from "react";
export const CategoryNavTabs = (props: any) => <div {...props} />;
""")
    with open(os.path.join(test_dir, "src", "components", "customer", "MenuItemGrid.tsx"), "w", encoding="utf-8") as f:
        f.write("""import React from "react";
export const MenuItemGrid = (props: any) => <div {...props} />;
""")
    with open(os.path.join(test_dir, "src", "components", "customer", "FloatingCartBar.tsx"), "w", encoding="utf-8") as f:
        f.write("""import React from "react";
export const FloatingCartBar = (props: any) => <div {...props} />;
""")
    with open(os.path.join(test_dir, "src", "components", "customer", "SkeletonMenuLoading.tsx"), "w", encoding="utf-8") as f:
        f.write("""import React from "react";
export const SkeletonMenuLoading = (props: any) => <div {...props} />;
""")

    print("\nRunning 'npm install' in ts_verification...")
    res_npm = subprocess.run(["npm", "install", "--prefer-offline", "--no-audit"], cwd=test_dir, shell=True, capture_output=True, text=True)
    print("NPM returncode:", res_npm.returncode)
    if res_npm.returncode != 0:
        print("NPM STDERR:", res_npm.stderr)

    print("\nRunning 'npx tsc --noEmit' in ts_verification...")
    res_tsc = subprocess.run(["npx", "tsc", "--noEmit"], cwd=test_dir, shell=True, capture_output=True, text=True)
    print("TSC STDOUT:\n", res_tsc.stdout)
    if res_tsc.stderr:
        print("TSC STDERR:\n", res_tsc.stderr)
    print(f"Exit code: {res_tsc.returncode}")
    return res_tsc.returncode == 0

if __name__ == "__main__":
    success = setup_and_typecheck_ts()
    print("TYPESCRIPT TYPECHECK TEST:", "PASS" if success else "FAIL")
