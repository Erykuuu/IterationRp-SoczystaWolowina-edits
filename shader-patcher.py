import os
import sys
import subprocess
import shutil

# ITRPedit Shader Patcher v1.10
# Designed to apply .diff patches to iterationRP Alpha 0.8.18 baseline

def patch_shaders():
    print("=== ITRPedit Shader Patcher v1.10 ===")
    
    # 1. Identify paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    patch_file = os.path.join(base_dir, "ITRPeditV1.10.diff")
    
    if not os.path.exists(patch_file):
        print(f"Error: Patch file '{patch_file}' not found in the same directory as this script.")
        return

    # Look for 'shaders' folder in parent directory or current directory
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
        print("Error: Could not find 'shaders' directory.")
        print("Please place the 'dist' folder inside your shaderpack root or alongside the 'shaders' folder.")
        return

    print(f"Target found: {target_dir}")
    
    # 2. Check for git (easiest way to apply complex binary diffs)
    try:
        # We use git apply with --directory to point to the shaders parent
        # Since our diff was made with 'temp_orig/shaders' vs 'ITRPedit/shaders', 
        # it expects a 'shaders' folder prefix.
        
        parent_of_shaders = os.path.dirname(target_dir)
        
        print("Applying patch...")
        # -p1 strips the first path component (temp_orig/ITRPedit)
        # --unidiff-zero allows empty files/new files if needed
        # --verbose gives us feedback
        result = subprocess.run(
            ["git", "apply", "-p1", "--verbose", patch_file],
            cwd=parent_of_shaders,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("Successfully patched!")
            print(result.stdout)
        else:
            print("Patch failed!")
            print(result.stderr)
            print("\nTroubleshooting:")
            print("1. Ensure you are patching a CLEAN 'iterationRP Alpha 0.8.18' version.")
            print("2. Ensure Git is installed and in your PATH.")
            
    except FileNotFoundError:
        print("Error: 'git' command not found. This patcher requires Git to be installed to handle binary data (LUTs).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    patch_shaders()
    input("\nPress Enter to exit...")
