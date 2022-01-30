import subprocess
import pexpect

def run_script(commands):
    cmd = pexpect.spawn('./cdatabase mydb.db', encoding='utf-8')
    cmd.logfile = open('test/test.log', 'w')
    for i,input in enumerate(commands):
        cmd.expect('db >')
        cmd.sendline(input)
    txt = cmd.read()
    cmd.close()
    return txt

def run_script_subprocess(commands):
    command = '\n'.join(commands) + '\n'
    cmd = subprocess.Popen(['./repl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    res = cmd.communicate(command.encode())[0]
    return res.decode()

def table_full_test():
    script = [f"insert {i} user{i} person{i}@example.com" for i in range(1,1402)]
    script.append(".exit")
    return script

def max_string_length():
    long_username = 'a'*25
    long_email = 'a'*255
    script = [
        f"insert into user values 1 {long_username} {long_email}",
        "select",
        ".exit",
    ]
    return script

lst = ['insert 1 user1 person1@example.com', 'select', '.exit']
cmd = run_script(max_string_length())
ls = []
with open('test/test.log', "r") as f:
    lines = f.readlines()
    for line in lines:
        if(line[:2] != "db"):
           ls.append(line)
with open('test/test.log', "w") as f:
    f.write(''.join(ls))