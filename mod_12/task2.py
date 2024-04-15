import subprocess

def process_count(username: str) -> int:
    args=['ps', '-u', username, '-o', 'pid']
    process=subprocess.run(args, capture_output=True)
    list_processes=process.stdout.decode().splitlines()[1:]
    return len(list_processes)

def total_memory_usage(root_pid: int) -> float:
    args=['ps', '--ppid', str(root_pid), '-o', '%mem=']
    process=subprocess.run(args, capture_output=True)
    list_processes=process.stdout.decode().splitlines()
    new_list=[float(i) for i in list_processes]
    return new_list

if __name__=='__main__':
    count=process_count('admin')
    print(f"кол-во процессов под пользователем 'admin'- {count}")
    memory=total_memory_usage(1)
    print(f"суммарное подребление памяти дерева процессов с PPID=1- {memory}%")