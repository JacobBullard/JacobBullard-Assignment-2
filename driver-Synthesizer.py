"""At this point in the application file structure, two files exist in our application
one that synthesizes a plain text file. 

This is authored by Jacob Bullard Computer Security Spring 2023"""

cipher_key_length = 7

from Synthesizer import analyze_frequency_bit_pattern

# In the beginning
gibberish = open("cipher_text.txt", "rb") # opening for [r]eading as [b]inary
encoded_data = gibberish.read() # if you only wanted to read 512 bytes, do .read(512)

# Between now and the beginning, I've been using StackOverFlow.
# .....and running into errors
# Let's hope this thread is actually helpful. 
# https://stackoverflow.com/questions/6787233/python-how-to-read-bytes-from-file-and-save-it

#                #
#  W S E K O F P #
#                #
#  A E I N O S T #
#                #
#  B D E F O M Y #

print("At this point in the code, we have read the ciphertext, as binary into a list of bytes, here are those bytes: ")
print()
print(str(encoded_data))
print()

ordered_gibberish_patterns = []

population_size = 0

# this part of code performs frequency analysis on our gibberish
for byte in analyze_frequency_bit_pattern(encoded_data):
    ordered_gibberish_patterns.append(str(byte))
    population_size = population_size + analyze_frequency_bit_pattern(encoded_data).get(byte)
print()

# encrypt with keys here
#
# 
#
#

key = "yz"

for byte in analyze_frequency_bit_pattern(encoded_data):
    # THE ENCODING HAPPENING HERE APPEARS TO BE ASCII ASSUMED
    # WHAT PART OF AN OPERATING SYSTEM ARCHITECTURE NEEDS TO 
    # KNOW 
   
    print( "Byte: " + str(byte) + " had frequency " + str(int(str(analyze_frequency_bit_pattern(encoded_data).get(byte)))*100/ +
    population_size))

print()

# this statement here is beautiful
# I wanna see how the computers memory spins
num_bytes =len(analyze_frequency_bit_pattern(encoded_data))
print(str(num_bytes) + " 'different' patt3rns found\n")

# print("Upon further analysis of the binary;")
# print("A pattern of 7 consecutive bytes detected.") 
# print("The bytes in the ciper text 'XISZMNM' appear twice.")
# print()
# print("There was a pattern of 4 consecutive bytes detected.")
# print("The bytes in the ciper text 'VFGO' appear twice.")

print()
#The key length is 7

relative_frequency_ciper_7kATTACK  =  b"SPWOEKF"
relative_frequency_key             =  b"ETAOINSRHDLUCMFYWGPBVKXQJZ"

print("The relative frequency of our ciphertext looks like")
#print(relative_frequency_ciper) 

print()
print("The relative frequency of bytes looks like")
#frequency_key here is a pre-generated 'expected' pattern of 42 bits to match 
print(relative_frequency_key)
print("One could imply substitution of every cipher text")  
print(relative_frequency_ciper_7kATTACK)

# for byte in analyze_frequency_bit_pattern(encoded_data):
#     # THE ENCODING HAPPENING HERE APPEARS TO BE ASCII ASSUMED
#     # WHAT PART OF AN OPERATING SYSTEM ARCHITECTURE NEEDS TO 
#     # KNOW 


### Decrypt / Decode here 
decrypted_data = []
decrypted_string =""
for function_one in encoded_data:

    found_match = False

    for function_two in relative_frequency_ciper_7kATTACK:
        if function_one == function_two:
            found_match = True
            print("Input: " + str(function_one) + " detected")
            decrypted_data.append(str(relative_frequency_key[relative_frequency_ciper_7kATTACK.index(function_one)]))
            #magic hash here
            decrypted_string = decrypted_string + str(relative_frequency_key[relative_frequency_ciper_7kATTACK.index(function_one)])
            print("substituted with " + str(relative_frequency_key[relative_frequency_ciper_7kATTACK.index(function_one)]))
            break
    if found_match == False:
        decrypted_string = decrypted_string + str(byte)
        found_match = False
    
    


print()

print("New Message: ")

print(str(decrypted_string))

# This function is MAGIC
# seems like it should apply the key to the text
# for b in encoded_data:
#     #replace byte in cipher text with a good guess and then run the 
#     print("cipher-pattern: " + str(b)) 
#     print("changed-to: " + str(key_list.index(b)) + " " + str(key_list[key_list.index(b)]))

print()
    
"""Assemble them all together now and this defines
our population/domain_space-ish/physical_to_neuro"""
block_text = """
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################"""
#print(block_text) - wow it works
print("Population Size or Sample Amount or Time Duration or Sensor Measurement: " + str(population_size))
print("Population Size or Sample Amount or Time Duration or Sensor Measurement: " + str(len(decrypted_string)))


def longest_repeated_substring(text):
    n = len(text)
    suffixes = sorted([text[i:] for i in range(n)])
    lrs = ""
    for i in range(n - 1):
        lcp = common_prefix(suffixes[i], suffixes[i + 1])
        if len(lcp) > len(lrs):
            lrs = lcp
    return lrs

def common_prefix(a, b):
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    return a[:i]

text = "WCBSIOOPAYVDEZWJYKOR"
print("Longest repeating substring:", longest_repeated_substring(text))