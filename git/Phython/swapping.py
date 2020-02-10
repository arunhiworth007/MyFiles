Count= int(input("Enter How many Numbers"))
a=[]
for i in range(0,Count,1):
    a.append(input('Enter value of {} = '.format(i+1)))
noofrides = int(input('enter number of rides'))
for i in range(noofrides):   
    try:
        
        firstposition =int(input('enter First postion'))-1
        secondposition = int(input('enter second swap postion'))-1
    except:
        pass
    a[firstposition], a[secondposition] = a[secondposition], a[firstposition]
                
                
print('-------------------------------------------')
print('The final List',a)           
                
