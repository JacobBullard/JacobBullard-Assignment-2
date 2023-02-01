# In the beginning, there was a file/split of energy/light
# 
# 
# 
from collections import Counter

def deCode(_binary_stream):
    # Step 1: Store the # of times we observe/feel-neuro/sense each thang
    bytes = Counter(_binary_stream)

    # Step 2: Sort the bytes by popularity
    order_bytes = dict(sorted(bytes.items(), key=lambda x: x[1], reverse=True))

    # Step 3: Return the sorted frequency count
    return order_bytes