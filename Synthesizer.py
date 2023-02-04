# In the beginning, there was a file/split of energy/light
# 
# 
# 
from collections import Counter
num_bytes_read = 0

def analyze_frequency_bit_pattern(_binary_stream):
    # Step 1: Store the # of MeM Configs, mem capacity, Object, 
    #  we capture. Clock and physics come into play att
    bytes = Counter(_binary_stream)

    # Step 2: Sort the bytes by popularity
    order_bytes = dict(sorted(bytes.items(), key=lambda x: x[1], reverse=True))

    num_bytes_read = len(order_bytes)

    # Step 3: Return the sorted frequency count
    return order_bytes