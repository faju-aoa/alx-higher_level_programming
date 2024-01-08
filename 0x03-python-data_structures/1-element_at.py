#!/usr/bin/python3
def element_at(my_list, idx):
  g= [i for i in my_list]
  if idx < 0:
    return None
  elif idx > len(g):
    return None
  else:
   return g[idx]
