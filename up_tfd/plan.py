import sys
import os
import subprocess

def main():
    if len(sys.argv) != 4:
        exit(0)
    
    domain_filename, problem_filename, plan_filename = sys.argv[1:4]
    
    tfd_executable = os.path.join(os.environ.get('TFD_HOME'), 'downward', 'plan')
    os.chdir(os.path.dirname(tfd_executable))
    cmd = ['/bin/bash', tfd_executable, domain_filename, problem_filename, plan_filename]
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    process.communicate()
    retval = process.returncode
    exit(retval)

if __name__ == '__main__':
    main()