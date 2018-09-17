
# coding: utf-8

# In[ ]:


def bubbleSort (alist):
    for passnum in range(len (alist)-l,0,-l):
        for i in range (passnum):
            if alist[i]>alist[i+l]:
                temp = alist [1] 
                alist[i] = alist[i+1]
                alist[i+1] = temp
alist=[54,26,93,17,77,31,44,55,20]
bubbleSort (alist)
print(alist)

