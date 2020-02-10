Count= int(input("Enter How many Numbers"))
a=[]
for i in range(0,Count,1):
    a.append(int(input('Enter value of {} = '.format(i+1))))
s = set(a)
lst = list(s)
print('-------------------------------------------')
for i in range(0,len(lst),1):
    print('The Count for ', lst[i],'is ',a.count(lst[i]))
print('Done')
