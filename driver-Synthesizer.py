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
print("Beginning Synthesation")
print()
print("""At this point in the code, we have read the ciphertext(garbled signal) as binary, 
classified each 'component' of the signal. This will allow us to form a basis for repeated behavior.""")
print()
print(str(encoded_data))

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
    print( "Encoded Byte: " + str(byte) + " had frequency " + str(int(str(analyze_frequency_bit_pattern(encoded_data).get(byte)))*100/ +
    population_size))

print()

# this statement here is beautiful
# I wanna see how the computers memory spins [STACK RESEARCH gdb- [project 2]]
num_bytes =len(analyze_frequency_bit_pattern(encoded_data))
print(str(num_bytes) + " 'different' patt3rns found\n")

# print("Upon further analysis of the binary;")
# print("A pattern of 7 consecutive bytes detected.") 
# print("The bytes in the ciper text 'XISZMNM' appear twice.")
# print()
# print("There was a pattern of 4 consecutive bytes detected.")
# print("The bytes in the ciper text 'VFGO' appear twice.")

print()

relative_frequency_ciper  =           b"SPWOEKFMBZG" # relative_frequency_jammer =           b"DXVIYACQLHJ"
relative_frequency_key    =           b"ETAOINSRHDL"


print("The relative frequency of our ciphertext looks like")
print(relative_frequency_ciper)
print()
print("One could imply substitution of every cipher text(gibberish pattern) with its expected frequency match")  
print(relative_frequency_key)

### Synthesize happens here here 
### TODO Make this a helper driver

decrypted_data = []
hashed_functions =""
#match signals (==apply hash?== bleichan?)
for function_one in encoded_data:
    found_match = False
    for function_two in relative_frequency_ciper:
        # if we have a match in signal
        if function_one == function_two:
            found_match = True
            #print("Input: " + str(function_one) + " detected")
            decrypted_data.append(str(relative_frequency_key[relative_frequency_ciper.index(function_one)]))
            #magic hash here
            hashed_functions = str(hashed_functions) + str(relative_frequency_key[relative_frequency_ciper.index(function_one)]) + " "
            #print(" substituted with " + str(relative_frequency_key[relative_frequency_ciper.index(function_one)]))
            break
    if found_match == False:
        hashed_functions = hashed_functions + str(byte) + " "
        found_match = False
print()

print("New Message: ")
print(hashed_functions)
print()

"""Analyze the frequency after compressing the two functions"""
# gibberish = open("cipher_text_compress.txt", "rb") # opening for [r]eading as [b]inary
# encoded_data = gibberish.read() # if you only wanted to read 512 bytes, do .read(512)

# for byte in decrypted_string:
#     # THE ENCODING HAPPENING HERE APPEARS TO BE ASCII ASSUMED
#     # WHAT PART OF AN OPERATING SYSTEM ARCHITECTURE NEEDS TO 
#     # KNOW 
   
#     print( "Original ciphertext: " + str(ordered_gibberish_patterns.index(str(byte))) + " changed to: " + str(byte))
# print()

print("""At this point in the code, we have read an input(signal) as binary, 
classified each 'component' of the signal and determined the frequency of each component. 
We then match the overall input(signal) dataset with something of its 'kind', in 
hopes to (bring order to)[make 'sense'()](classify) input data.""")
print()
#print(str(decrypted_data))
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
#print("Population Size or Sample Amount or Time Duration or Sensor Measurement: " + str(len(decrypted_string)))


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

# text = "WCBSIOOPAYVDEZWJYKOR"
# print("Longest repeating substring:", longest_repeated_substring(text))