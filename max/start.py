import subprocess
import os


projectPath = os.path.dirname(__file__)
commands = '''
dir; cd {0}; dir;
'''.format(projectPath)
# process = subprocess.Popen(commands, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

# commands.encode('utf-8')
#
# subprocess.call("dir", shell=True)
# out,err = process.communicate()
# print(out)
wd = os.getcwd()
print(wd)
os.chdir(projectPath)
wd = os.getcwd()
print(wd)
os.system(r"python manage.py runserver")
# subprocess.check_call("pip install requirements.txt python manage.py runserver", cwd=projectPath, shell=True)
# subprocess.call("", shell=True)
# command = "cd {} & python manage.py runserver".format(projectPath)
# print("executing {}".format(command))
# subprocess.call(command, shell=True)