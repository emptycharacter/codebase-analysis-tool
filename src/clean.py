import os
import subprocess
import radon.complexity as radon_cc
import ast


def get_python_files():
    """Find all Python files in the current directory and subdirectories."""
    python_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def remove_unused_imports_and_format(files):
    """Removes unused imports and formats the code using autoflake and black."""
    for file in files:
        subprocess.run(
            [
                "autoflake",
                "--in-place",
                "--remove-unused-variables",
                "--remove-all-unused-imports",
                file,
            ]
        )

    print("✅ Unused imports and variables removed.")
    subprocess.run(["black", "."])
    print("✅ Code formatting complete!")


def detect_large_functions(files):
    """Detects and warns about large functions in the code."""
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            source_code = f.read()
        tree = ast.parse(source_code)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                line_count = node.end_lineno - node.lineno + 1
                if line_count > 50:  # Warn if a function is too large
                    print(
                        f"⚠️ Warning: Large function detected in {file}: {node.name} ({line_count} lines)"
                    )


def detect_complexity(files):
    """Uses radon to detect complex functions that might need refactoring."""
    for file in files:
        print(f"\n🔍 Checking complexity in: {file}")
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        results = radon_cc.cc_visit(code)
        for item in results:
            if item.complexity > 10:  # Threshold for "too complex"
                print(
                    f"⚠️ Complex function: {item.name} in {file} (Complexity: {item.complexity})"
                )


def run():
    print("🔹 Starting code cleanup process...")
    python_files = get_python_files()

    if not python_files:
        print("No Python files found to clean.")
        return

    print(f"📂 Found {len(python_files)} Python files. Cleaning them now...\n")

    # Step 1: Remove unused imports and format code
    remove_unused_imports_and_format(python_files)

    # Step 2: Detect large functions
    detect_large_functions(python_files)

    # Step 3: Detect complex functions
    detect_complexity(python_files)

    print("\n✅ Code cleanup complete!")


if __name__ == "__main__":
    run()
