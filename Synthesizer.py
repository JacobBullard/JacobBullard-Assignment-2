# In the beginning, there was a file/split of energy/light
# 
# 
# 
from collections import Counter

def count_them_thangs(what_is_this):
    # Step 1: Store the # of times we observe/feel-neuro/sense each thang
    diffrant_thangs = Counter(what_is_this)

    # Step 2: Sort the thangs by popularity
    ranked_thangs = dict(sorted(diffrant_thangs.items(), key=lambda x: x[1], reverse=True))

    # Step 3: Return the sorted frequency count
    return ranked_thangs

ciphertext = "hllwrdlwryld"
print(count_them_thangs(ciphertext))