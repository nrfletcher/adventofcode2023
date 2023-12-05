import os, sys, subprocess

def run_script(script_filename, *args):
    script_path = os.path.join("pysolutions", script_filename)
    try:
        subprocess.run(["python", script_path] + list(args), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <script_name>")
        sys.exit(1)
    
    script_name = sys.argv[1]
    script_args = sys.argv[2:]
    run_script(script_name, *script_args)