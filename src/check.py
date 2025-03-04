import os
import subprocess

def check_code_security():
    """Runs Bandit to scan for security vulnerabilities in Python code."""
    print("🔍 Scanning Python code for security risks...")
    subprocess.run(["bandit", "-r", "src/", "tests/"])
    print("✅ Code security scan complete.")

def check_dependency_vulnerabilities():
    """Checks installed Python dependencies for known security issues."""
    print("🔍 Checking dependencies for vulnerabilities...")
    subprocess.run(["safety", "check", "--full-report"])
    print("✅ Dependency security check complete.")

def run():
    """Runs all security checks."""
    print("🚨 Running security checks...")
    check_code_security()
    check_dependency_vulnerabilities()
    print("✅ All security checks completed!")

if __name__ == "__main__":
    run()
