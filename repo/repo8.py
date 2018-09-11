(/, Simple, stream, input/output)
#include <iostream.h>

main()
{
cout << "Enter your age: "; 
int myAge;
cin >> myAge;

cout << "Enter your friend's age: "; 
int friendsAge;
cin >> friendsAge;

if (myAge > friendsAge)
    cout << "You are older.\n"; 
else
    if (myAge < friendsAge)
        cout << "You are younger.\n"; 
    else
        cout << "You and your friend are the same age.\n";

return O;
}
