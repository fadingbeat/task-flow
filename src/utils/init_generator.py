import os

def create_init_files(start_dir='.'):
    """Recursively create __init__.py files in all subdirectories."""
    for dirpath, dirnames, filenames in os.walk(start_dir):
        # Skip directories like virtual environments (optional)
        if 'venv' in dirpath:
            continue
        
        # Generate __init__.py in each directory
        init_file = os.path.join(dirpath, '__init__.py')
        # Create __init__.py if it doesn't exist
        if not os.path.exists(init_file):
            with open(init_file, 'a'):
                pass  # Create an empty __init__.py file
            print(f"Created: {init_file}")  # Optional: print the path of created files

if __name__ == "__main__":
    create_init_files(os.path.join(os.path.dirname(__file__), '..'))  # Start from the project root
