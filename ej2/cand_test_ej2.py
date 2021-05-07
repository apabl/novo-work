import re

def run():
    with open('testcase.v') as f:
        content = f.read()

    partdata = re.search(r'^((.*\n)+)(  initial begin\n)((    \S*\[\S*\] = \S*;\n)*)(  end\n)((.*\n)+)$',
                         content)

    with open('expected_ej2.v', 'w') as file_expected:
        file_expected.write(partdata.group(1))
        file_expected.write('  $readmemh("memdump0.mem", mem);\n')
        file_expected.write(partdata.group(7))

    with open('memdump0.mem', 'w') as file_memdump:
        
        for line in partdata.group(4).splitlines():
            file_memdump.write(f"{line[-3:-1]}\n")

if __name__ == "__main__":
    run()