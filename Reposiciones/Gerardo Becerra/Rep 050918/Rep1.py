
# coding: utf-8

# In[ ]:


def mergeSort: (alist):
    print ("Splitting ",alist)
    if len(alist)>l:
        mid = len (alist)//2 
        lefthalf = alist[:mid ] 
        righthalf = alist [mid:]

        mergeSort (lefthalf) 
        mergeSort (righthalf)

        i=0 
        j=0 
        k=0
        while i<len (lefthalf) and j<len (righchalf): 
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+l 
            else :
                alist[k]=righthalf[j]
                j=j+l
            k=k+l

        while i<len (lefThalf): 
            alist[k]=lefthalf[i]
            i=i+l
            k=k+l

        while j<len (righthalf): 
            alist [k]=righthalf[j] 
            j=j+l
            k=k+l

print "Resultado: ",(alist)

