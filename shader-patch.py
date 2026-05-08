import os
import sys
import subprocess
import shutil
import zipfile
import tempfile

# ITRPedit Shader Patcher v1.10
# Enhanced version: supports ZIP processing via command line arguments

def apply_patch(target_dir, patch_file):
    """Applies the .diff patch to the target directory using git apply."""
    try:
        # We assume the diff has a 'shaders/' prefix
        # We need to run git apply in the directory containing 'shaders/'
        
        # Check if target_dir itself is 'shaders' or contains 'shaders'
        if os.path.basename(target_dir) == "shaders":
            working_dir = os.path.dirname(target_dir)
        else:
            working_dir = target_dir

        print(f"Applying patch using Git in: {working_dir}")
        
        # Try different path stripping levels (-p1 and -p2) to find the one that matches
        for p_level in ["-p2", "-p1"]:
            print(f"Trying patch with {p_level}...")
            result = subprocess.run(
                ["git", "apply", p_level, "--verbose", os.path.abspath(patch_file)],
                cwd=working_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"Successfully patched using {p_level}!")
                print(result.stdout)
                return True
            else:
                last_error = result.stderr
        
        print("Patch failed at all levels!")
        print(last_error)
        return False
            
    except FileNotFoundError:
        print("Error: 'git' command not found. This patcher requires Git to be installed.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during patching: {e}")
        return False

def zip_dir(path, zip_filename):
    """Zips the contents of a directory."""
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, path)
                zipf.write(abs_path, rel_path)

def main():
    print("=== ITRPedit Shader Patcher v1.10 ===")
    
    # CASE 1: Command line arguments (ZIP processing)
    if len(sys.argv) == 4:
        orig_zip = sys.argv[1]
        patch_file = sys.argv[2]
        out_zip = sys.argv[3]
        
        if not os.path.exists(orig_zip):
            print(f"Error: Original ZIP '{orig_zip}' not found.")
            return
        if not os.path.exists(patch_file):
            print(f"Error: Patch file '{patch_file}' not found.")
            return

        with tempfile.TemporaryDirectory() as tmpdir:
            print(f"Extracting {orig_zip}...")
            with zipfile.ZipFile(orig_zip, 'r') as zip_ref:
                zip_ref.extractall(tmpdir)
            
            if apply_patch(tmpdir, patch_file):
                print(f"Creating patched ZIP: {out_zip}...")
                zip_dir(tmpdir, out_zip)
                print("Done! Patched ZIP created successfully.")
            else:
                print("Failed to create patched ZIP.")

    # CASE 2: No arguments (Interactive/Automatic directory discovery)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        patch_file = os.path.join(base_dir, "ITRPeditV1.10.diff")
        
        if not os.path.exists(patch_file):
            print(f"Error: Patch file '{patch_file}' not found in the same directory as this script.")
            print("Usage: python shader-patch.py <original_zip> <diff_file> <output_zip>")
            return

        # Look for 'shaders' folder
        target_dir = None
        possible_paths = [
            os.path.join(base_dir, "shaders"),
            os.path.join(os.path.dirname(base_dir), "shaders"),
            os.path.join(base_dir, "ITRPedit", "shaders")
        ]
        
        for path in possible_paths:
            if os.path.exists(path) and os.path.isdir(path):
                target_dir = path
                break
                
        if not target_dir:
            print("Error: Could not find 'shaders' directory for automatic patching.")
            print("Please provide ZIP files as arguments or place script next to 'shaders' folder.")
            print("Usage: python shader-patch.py <original_zip> <diff_file> <output_zip>")
            return

        apply_patch(target_dir, patch_file)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
