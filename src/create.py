import os
import ast

def extract_docstrings(file_path):
    """Extracts function and class docstrings from a Python file."""
    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()
    
    tree = ast.parse(source_code)
    doc_data = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):  # Find functions
            func_name = node.name
            docstring = ast.get_docstring(node) or "No docstring provided."
            doc_data.append(f"### Function: `{func_name}()`\n\n{docstring}\n")
        elif isinstance(node, ast.ClassDef):  # Find classes
            class_name = node.name
            docstring = ast.get_docstring(node) or "No docstring provided."
            doc_data.append(f"## Class: `{class_name}`\n\n{docstring}\n")
    
    return doc_data

def generate_docs():
    """Generates documentation for all Python files in the project."""
    python_files = []
    
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py") and "test_" not in file:  # Skip test files
                python_files.append(os.path.join(root, file))

    if not python_files:
        print("No Python files found for documentation.")
        return

    # Create docs/ folder if it doesn't exist
    os.makedirs("docs", exist_ok=True)

    for file in python_files:
        doc_content = extract_docstrings(file)
        if not doc_content:
            continue  # Skip files with no docstrings
        
        file_name = os.path.basename(file).replace(".py", ".md")
        doc_path = os.path.join("docs", file_name)

        with open(doc_path, "w", encoding="utf-8") as doc_file:
            doc_file.write("# Documentation\n\n")
            doc_file.writelines(doc_content)

        print(f"📄 Documentation generated: {doc_path}")

def run():
    print("📝 Generating documentation...")
    generate_docs()
    print("✅ Documentation process complete!")

if __name__ == "__main__":
    run()

