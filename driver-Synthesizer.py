"""At this point in the application file structure, two files exist in our application
one that synthesizes a plain text file. 

This is authored by Jacob Bullard Computer Security Spring 2023"""


from Synthesizer import deCode

# In the beginning
gibberish = open("cipher_text.txt", "rb") # opening for [r]eading as [b]inary
encoded_data = gibberish.read() # if you only wanted to read 512 bytes, do .read(512)

# Between now and the beginning, I've been using StackOverFlow.
# .....and running into errors
# Let's hope this thread is actually helpful. 
# https://stackoverflow.com/questions/6787233/python-how-to-read-bytes-from-file-and-save-it

num_bytes =len(deCode(encoded_data))

cipher_key = "SPWOEKFMBZGDXVIYACQLHJRTUN"
frequency_key = "ETAOINSRHDLUCMFYWGPBVKXQJZ"

decoded_message = ""

print(cipher_key[0])
print(frequency_key[0])

print(str(num_bytes) + " diffrant thangs found\n")

print(str(encoded_data))

print()

population_size = 0
byte_list = []
for byte in deCode(encoded_data):
    byte_list.append(str(byte))
    population_size = population_size + deCode(encoded_data).get(byte)
    print("Byte: " + str(byte) + " was detected " + str(deCode(encoded_data).get(byte)) + " times.")

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

print()

cipher_text_decoded = ""
for i in range(len(byte_list)):
    cipher_text_decoded = cipher_text_decoded + byte_list[i] + " "
# 
# Houston, we are going to need a map and a compass, on second thought, forget the compass. 
# 

print(cipher_text_decoded)