"""At this point in the application file structure, two files exist in our application
one that synthesizes a plain text file. 

This is authored by Jacob Bullard Computer Security Spring 2023"""

from Synthesizer import analyze_frequency_bit_pattern

# In the beginning
gibberish = open("cipher_text.txt", "rb") # opening for [r]eading as [b]inary
encoded_data = gibberish.read() # if you only wanted to read 512 bytes, do .read(512)

# Between now and the beginning, I've been using StackOverFlow.
# .....and running into errors
# Let's hope this thread is actually helpful. 
# https://stackoverflow.com/questions/6787233/python-how-to-read-bytes-from-file-and-save-it

hacked_key =    b"SPWOEKFMBZGDXVIYACQLHJRTUN" 

frequency_key = b"ETAOINSRHDLUCMFYWGPBVKXQJZ"
#
#  W S E K O F P #
#
#  A E I N O S T #




decoded_message = ""

print(str(encoded_data))

print()

# this statement here is beautiful
# I wanna see how the computers memory spins
num_bytes =len(analyze_frequency_bit_pattern(encoded_data))

print(str(num_bytes) + " bytes found\n")

population_size = 0
byte_list = []
key_list = []

for byte in analyze_frequency_bit_pattern(frequency_key):
    key_list.append(str(byte))

for byte in analyze_frequency_bit_pattern(encoded_data):
    byte_list.append(str(byte))
    population_size = population_size + analyze_frequency_bit_pattern(encoded_data).get(byte)
    print("Byte: " + str(byte) + " ocurred " + str(analyze_frequency_bit_pattern(encoded_data).get(byte)) + " times")
    
print()

for byte in analyze_frequency_bit_pattern(encoded_data):
    # THE ENCODING HAPPENING HERE APPEARS TO BE ASCII ASSUMED
    # WHAT PART OF AN OPERATING SYSTEM ARCHITECTURE NEEDS TO 
    # KNOW 
    print("Byte: " + str(byte) + " had frequency " + str(int(str(analyze_frequency_bit_pattern(encoded_data).get(byte)))*100/ +
    population_size))

print()




# This function is MAGIC
# seems like it should apply the key to the text
for b in byte_list:

    #if b matches with another b
    print("cipher-secret: " + str(byte_list.index(b)) + " " + b) 
    print("key: " + str(key_list.index(b)) + " " + str(key_list[key_list.index(b)]))



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
