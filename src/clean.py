import os
import subprocess


def run():
    print("Cleaning code...")

    # Find all Python files in the current directory and subdirectories
    python_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    if not python_files:
        print("No Python files found to clean.")
        return

    print(f"Found {len(python_files)} Python files. Cleaning them now...")

    # Step 1: Remove unused imports using autoflake
    for file in python_files:
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

    # Step 2: Format code using Black
    subprocess.run(["black", "."])

    print("✅ Code formatting complete!")


if __name__ == "__main__":
    run()
