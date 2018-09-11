
# coding: utf-8

# In[ ]:


#include <iostream.h>
struct Time {  structure definition int hour;
int minute;	
int second;
} ;
void printMilitary(const Time &); 
void printStandard(const Time &);
main()
{
    Time dinnerTime; // variable of new type Time
// set members to valid values 
    dinnerTime.hour =  18;
    dinnerTime.minute = 30; 
    dinnerTime.second =  O;
    
    cout << "Dinner will be held at "; 
    printMilitary(dinnerTime) ;
    cout << " military time,\nwhich is ";
    printStandard(dinnerTime);
    cout << " standard time." < < endl;

// set members to invalid values 
    dinnerTime.hour =  29;
    dinnerTime.minute =  73; 
    dinnerTime. second =  103;
    
    cout < < "\nTime with invalid values: "; 
    printMilitary(dinnerTime);
    cout << endl; 
    return O;

// Print the time in military format 
    void printMilitary( const Time &t)
{
cout << ((t.hour -- o   1  1    t.hour -- 12) ?   12 : t.hour %   12)
    << (t.minute < 10 ?  " º "  : " " )    << t.minute
    << (t.second < 10 ?   " 0 "    : " " )  << t.second
    << (t.hour < 12 ?  " AM"   : " PM" );
