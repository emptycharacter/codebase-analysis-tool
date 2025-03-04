import os
import subprocess
import re

def check_code_security():
    """Runs Bandit to scan for security vulnerabilities in Python code."""
    print("🔍 Scanning Python code for security risks...")
    subprocess.run(["bandit", "-r", "src/", "tests/"])
    print("✅ Code security scan complete.")

def check_dependency_vulnerabilities():
    """Checks installed Python dependencies for known security issues using the updated 'safety scan' command."""
    print("🔍 Checking dependencies for vulnerabilities using 'safety scan'...")
    subprocess.run(["safety", "scan"])
    print("✅ Dependency security check complete.")

def check_secrets():
    """Scans for hardcoded secrets like API keys, passwords, and tokens."""
    print("🔍 Scanning for hardcoded secrets...")
    secret_pattern = re.compile(r"(?i)(api[_-]?key|secret|password|token)[^\n]*['\"]([A-Za-z0-9_\-]{8,})['\"]")
    
    python_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    
    found_secrets = False
    for file in python_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            matches = secret_pattern.findall(content)
            if matches:
                found_secrets = True
                print(f"⚠️ Possible secrets found in {file}:")
                for match in matches:
                    print(f"   - {match[0]}: {match[1][:4]}... (masked for security)")
    
    if not found_secrets:
        print("✅ No hardcoded secrets found.")

def check_unsafe_functions():
    """Scans for dangerous Python functions like eval() and exec()."""
    print("🔍 Checking for unsafe function usage...")
    unsafe_patterns = ["eval(", "exec(", "pickle.load(", "subprocess.Popen(", "subprocess.run("]
    
    python_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    
    found_unsafe = False
    for file in python_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.readlines()
            for i, line in enumerate(content):
                for pattern in unsafe_patterns:
                    if pattern in line:
                        found_unsafe = True
                        print(f"⚠️ Unsafe function '{pattern.strip()}...' found in {file} (line {i+1})")
    
    if not found_unsafe:
        print("✅ No unsafe functions found.")

def run():
    """Runs all security checks."""
    print("🚨 Running security checks...")
    check_code_security()
    check_dependency_vulnerabilities()
    check_secrets()
    check_unsafe_functions()
    print("✅ All security checks completed!")

if __name__ == "__main__":
    run()

