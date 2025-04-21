#!/usr/bin/env python
# coding: utf-8

# In[2]:


diameter = 9
angle_degrees = 45
pi = 3.1416


# In[3]:


radius = diameter / 2


# In[4]:


angle_radians = (pi / 180) * angle_degrees
arc_length = radius * angle_radians


# In[5]:


print("Diameter of circle:", diameter)
print("Angle measure:", angle_degrees)
print("Arc Length is:", arc_length)

