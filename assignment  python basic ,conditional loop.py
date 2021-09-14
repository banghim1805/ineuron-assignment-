#!/usr/bin/env python
# coding: utf-8

# 
# # assignment1

# 1. Write a program which will find all such numbers which are divisible by 7 but are not amultiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printedin a comma-separated sequence on a single line.\
# 

# In[1]:


a=[]
for i in range(3200):
    if i >=2000 and i%5!=0 and i%7==0:
        a.append(i)
print(a)


# 2. Write a Python program to accept the user's first and last name and then getting themprinted in the the reverse order with a space between first name and last name.

# In[2]:


a=str(input("enter your first name"))
b=str(input("enter your last  name"))
print(a[::-1]," ",b[::-1])


# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r 3

# In[3]:


diameter=12
r=diameter/2

a=(4/3)*3.14*r*r*r

print("volume of sphere=",a,"cm cube")


# In[ ]:




