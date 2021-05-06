import re

def run():
    with open('testcase.v') as f:
        content = f.read()

    partdata = re.search(r'^((.*\n)+)(  initial begin\n)((    \S*\[\S*\] = \S*;\n)*)(  end\n)((.*\n)+)$',
                        content)

    with open('expected_ej2.v', 'w') as file:
        file.write(partdata.group(1))
        file.write('$readmemh("memdump0.mem", mem);\n')
        file.write(partdata.group(7))

if __name__ == "__main__":
    run()