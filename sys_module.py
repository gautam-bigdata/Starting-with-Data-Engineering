import sys
from pathlib import Path

# readme_file=Path('README.md')
# with open(readme_file,'r')as rm:
#     rm.readlines()


sys.path

for i in sys.path :
    print(i)

print(f'SYS ARGV- Giving python file path- {sys.argv}')

print(f'Length of sys.argv ={len(sys.argv)}')
if len(sys.argv)>=2:
    file=sys.argv[-1]
    with open (file) as f:
        file=f.readlines(500)

else :
    file ='File not found, Give file name correctly'

print(file)


print(f'SYS ARGV- Giving python file path- {sys.argv}')

print(f'Length of sys.argv ={len(sys.argv)}')
if len(sys.argv)>=2:
    file=sys.argv[-1]
    with open (file) as f:
        file=f.readlines(500)
    sys.exit()
else :
    file ='File not found, Give file name correctly'

print(file)

# Display Hook


print(sys.platform)
print(sys.version)
