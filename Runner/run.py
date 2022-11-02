import sys
import csv
import time
import os

result_file = sys.argv[1]
result_folder = os.path.dirname(result_file)
rows = [['Case ID', 'Result', 'comments', 'Log Path'], ['1', 'PASSED', 'THIS IS A PASSED CASE', ''],
        ['2', 'FAILED', 'A FAILED CASE', ''],
        ['3', 'FAILED', 'A FAILED CASE Folder', '']]
print('this is a test to generate result')
i = 0
while i <= 3:
    print("Test is on going {}s".format(i+1))
    # time.sleep(1)
    i += 1

with open(result_file, 'w') as csvfile:
    c_writer = csv.writer(csvfile)
    c_writer.writerows(rows)
print('Test finished !!!!!')
if not os.path.exists(result_folder):
    os.mkdir(result_folder)
case_folder = os.path.join(result_folder, '2')
if not os.path.exists(case_folder):
    os.mkdir(case_folder)

log_file_2 = os.path.join(case_folder, 'log2.txt')
with open(log_file_2, 'w') as fw2:
    fw2.write("case 2 is failed")
log_file_3 = os.path.join(result_folder, '3.log')
with open(log_file_3, 'w') as fw3:
    fw3.write("case 3 is failed")

sys.exit(0)
