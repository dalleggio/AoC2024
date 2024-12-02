#!/usr/bin/env python
# coding: utf-8

# In[32]:


def read_columns_to_lists(filename):
    """Reads two columns of numbers from a file into separate lists."""

    list1 = []
    list2 = []

    with open(filename, 'r') as file:
        for line in file:
            # Split the line into values (assuming space-separated)
            values = line.split()

            if len(values) >= 2:
                list1.append(int(values[0]))
                list2.append(int(values[1]))

    return list1, list2



# In[33]:


# Example usage
filename = "dec01-1.txt"
column1, column2 = read_columns_to_lists(filename)


# In[34]:


# Sort columns
column1.sort()
column2.sort()


# In[35]:


# subtract the two sorted lists
dist = [abs(x - y) for x, y in zip(column1, column2)]


# In[36]:


# add distances
total_dist = sum(dist)
print("total dist:", total_dist)


# In[37]:


# calculate list of similarity scores
sim_list = []
for x in column1:
    sim_list.append(x * column2.count(x))


# In[38]:


sim_score = sum(sim_list)
print("sim_score:", sim_score)


# In[ ]:



