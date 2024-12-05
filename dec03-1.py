#!/usr/bin/env python
# coding: utf-8

# In[13]:


import re
# Open data file and read it
filename = "data/dec03-1.txt"
lines = []
with open(filename, 'r') as file:
    for line in file:
        lines.append(line)

mult_acc = 0
p = re.compile('mul\(\d{1,3},\d{1,3}\)')        
for line in lines:
    inst_list = p.findall(line)
    for inst in inst_list:
        digits = inst[4:-1].split(',')
        mult_acc += int(digits[0]) * int(digits[1])
print('result part 1:', mult_acc)



# In[14]:


mult_acc = 0
p = re.compile('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
do = True
for line in lines:
    inst_list = p.findall(line)
    for inst in inst_list:
        if inst == "don't()":
            do = False
            continue
        if inst == "do()":
            do = True
            continue
        if do:
            digits = inst[4:-1].split(',')
            mult_acc += int(digits[0]) * int(digits[1])
print('result part 2:', mult_acc)            


# In[ ]:




