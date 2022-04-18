import subprocess
import sys

def run_cmd_sync(cmd):
    print("\nrun_cmd_sync begin ============================================================\n")
    subprocess.run(cmd, stderr=sys.stderr, stdout=sys.stdout)
    
    print("\nrun_cmd_sync end ============================================================\n\n")
