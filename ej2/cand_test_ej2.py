import re

with open('testcase.v') as f:
    content = f.read()

partdata = re.search(r'  reg \[(.*)\] (\S*) \[(.*)\];\n  initial begin\n((    \S*\[\S*\] = \S*;\n)*)  end\n',
                     content)

for g in range(5):
    print(partdata.group(g))