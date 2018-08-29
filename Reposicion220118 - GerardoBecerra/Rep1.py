
# coding: utf-8

# In[ ]:


(/CIRCLE.H)
Definition of class Circle
#ifndef CIRCLE_H
#define CIRCLE H

#include <iostream.h>
#include <iomanip.h>
#include "point.h"

class Circle : public Point { // Circle inherits from Point 
    friend ostream &operator< <(ostream &, const Circle &);
public:
    11 default constructor
    Circle(float r = O.O, float x = O, float y = O);
                             
    void setRadius(float); 
    float getRadius() const; 
    float area() const;
protected:
    float radius;
} ;

#endif

