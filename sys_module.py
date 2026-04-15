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




# need to sort this by removing duplicate 



def twopointer(l):
    k=0
    j=k+1
    while j<len(l):
        if l[k]==l[j]:
            l.pop(k)   
        else:
            k+=1
            j+=1
    return(l)

print(twopointer([2,4,4,4,5,6,7,7,8,8,8,8,8,8]))

# Sort the list to ascending order 

l=[1,1,2,2,2,2,4,5,6,8,6,7,5,3,2,33,2,2,2]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]<=l[j]:
            continue
        else:
            l[i],l[j]=l[j],l[i]
print(l)
