import subprocess
import time

python_path = tdu.expandPath(ipar.extLighting.Py)

# point to our script that we're going to execute
cmd_python_script = tdu.expandPath(ipar.extLighting.Script)

# point to the specific version of python that we want to use
python_exe = python_path

# pull IP and COM port
ip = str(parent(3).op('base_com/base_ip').par.Ip)
comPort = str(ipar.extLighting.Port)

# construct a list of arguments for out external script
script_args = ['-i', ip, '-i2', comPort]

# value to send
command_list = [python_exe, cmd_python_script] + script_args

# quick debug print
print(cmd_python_script)

# call our script with subprocess
subprocess.Popen(command_list, shell=True)

print('open')
