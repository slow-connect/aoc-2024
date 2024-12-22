import subprocess


def __load__(day):
    shell_script = ['./get_input.sh', str(day), str(2024)]
    try:
        output = subprocess.check_output(shell_script, stderr=subprocess.STDOUT, text=True)
        # If you want to capture both the output and the return code, you can use subprocess.run instead
        # process = subprocess.run(shell_script, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # output = process.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error while running the script: {e.returncode}\n{e.output}")
        output = None
    return str(output)


def get_str(day):
    str = __load__(day)
    return str

def get_lst(day):
    str = get_str(day)
    lst = str.split('\n')
    return lst

def get_int(day):
    lst = get_str(day).split('\n')
    it = []
    for k in range(len(lst)):
        if lst[k] != '':
            it.append(int(lst[k]))
    return it


def get_lst_of_lst(day):
    lst = get_str(day).split('\n')
    it = []
    k = 0
    tmp = []
    while k < len(lst):
        if lst[k] != '':
            tmp.append(lst[k])
        else:
            it.append(tmp)
            tmp = []
        k += 1
    return it

def pmap(data): print("\n".join("".join(c for c in line) for line in data))
