
# coding: utf-8

# In[ ]:


*(Using, strtok, */)
#include <stdio.h>
#include <string.h>

main()
{
char string[] =   "This is a sentence with 7 tokens"; 
char *tokenPtr;

printf("%s\n%s\n\n%s\n",
       "The string to be tokenized is:", string, 
       "The tokens are:");

tokenPtr = strtok(string, " "); 

while (tokenPtr ! =  NULL) {
    printf("% s\n" , tokenPtr);
    tokenPtr =  strtok(NULL, " ");
}

return O;
}

