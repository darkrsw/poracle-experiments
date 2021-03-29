#!/usr/bin/python
from datetime import datetime
import os
import shutil, sys
from os.path import join
import json
import time
import subprocess
array_to_follow = ['Patch48','Patch167','Patch196','Patch163','Patch25','Patch155','Patch175','Patch73','Patch160','Patch206','Patch191','Patch78','Patch20','Patch184','Patch207']
def run_cmd(cmd):
    try:
        code = os.system(cmd)
        return code
    except:
        return -1
def clean_up():
    cmd = 'rm -r ../traces/'
    os.system(cmd)
    cmd = 'rm -r ../test_coverage/'
    os.system(cmd)
    cmd = 'rm -r ../test_gen_randoop/'
    os.system(cmd)
    cmd = 'rm -r ../randoop_cover/'
    os.system(cmd)
    cmd = 'rm tmp*'
    os.system(cmd)
def run_experiment(configs_dir):
    for subroot, dirs, files in os.walk(configs_dir):
        # run('{}/cleanup'.format(root_dir))
        for config_file in files:
            read_file = open(join(configs_dir, config_file), "r")
            if (config_file.endswith('json') == False): continue
            if not config_file.startswith('Patch'): continue
            data = json.load(read_file)
            if data['ID'] not in array_to_follow: continue
            # for i in range(10):
            read_file = open(join(configs_dir, config_file), "r")
            data = json.load(read_file)
            # i = i + 1
            # print (i)
            st = data['project'] + ' ' + data['bug_id'] + ' ' + data['ID']
            for j in range(1, 4):
                clean_up()
                if os.path.exists(data['ID'] + '_exp' + str(j)):
                    continue
                cmd1 = 'python3 run_1000.py ' + st
                os.system(cmd1)
                cmd2 = 'timeout 20m python3 run_2000.py ' + st
                start_time = time.time()
                res = run_cmd(cmd2)
                end_time = time.time()
                elapsed_time = end_time - start_time
                time.sleep(1)
                if not os.path.exists(data['ID']):
                    continue
                f = open(data['ID'] + '/time', 'w')
                f.write(str(elapsed_time) + ' ' + str(res))
                f.close()
                cmd = 'mv ' + data['ID'] + ' ' + data['ID'] + '_exp' + str(j)
                os.system(cmd)




if __name__ == '__main__':
    configs_dir = '/poracle-experiments/configs/'
    run_experiment(configs_dir)

            #rename = 'mv ' + config_file +' ' + config_file+'_exp'+ str(i)
            #print(rename)
            # print(cmd)

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
