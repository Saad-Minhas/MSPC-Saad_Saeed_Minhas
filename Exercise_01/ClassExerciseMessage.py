#!/usr/bin/env python
# coding: utf-8

# In[25]:


from rich import print


# In[39]:


message_1 = "https://database.com/user/augustom,AugUSto Martin, 23, Approved,,"
message_2 = "https://database.com/user/juliasch,JuLIA SchmidT, 67, rejected,,"
message_3 = "https://database.com/user/kmarx,Karl Marx, 42, rejected,,"


# In[41]:


formated_m1 = message_1[26:].lower().replace(" ", "").removesuffix(",,")
formated_m2 = message_2[26:].lower().replace(" ", "").removesuffix(",,")
formated_m3 = message_3[26:].lower().replace(" ", "").removesuffix(",,")


# In[49]:


print (f"The formated message is \n{formated_m1} \n{formated_m2} \n{formated_m3}")

