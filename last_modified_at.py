import os
import re
from datetime import datetime


def get_modification_date(filename):
    stream = os.popen(f'git log -1 --pretty="format:%ci" {filename}')
    output = stream.read()
    return datetime.strptime(output, '%Y-%m-%d %H:%M:%S %z')


def update(filename, last_date, pattern, opt_name='mdate'):
    lines = []
    with open(filename, 'r') as fin:
        last_date_str = last_date.strftime('%b %d, %Y')
        lines = fin.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith(opt_name):
                result = pattern.search(line)
                date_from_file = result.group(0).strip('"')
                if date_from_file == last_date_str:
                    return
                print(f'{filename}:\t{date_from_file} -> {last_date_str}')
                lines[i] = f'{opt_name}: "{last_date_str}"\n'
                break
    with open(filename, 'w') as fout:
        fout.writelines(lines)


def process_dir(dir_path):
    filelist = os.listdir(dir_path)
    pattern = re.compile(r'\".*\"')
    for name in filelist:
        try:
            filepath = os.path.join(dir_path, name)
            mod_date = get_modification_date(filepath)
            update(filepath, mod_date, pattern)
        except Exception as e:
            print(str(e))


process_dir('./_notes')
