"""At this point in the application file structure, two files exist in our application
one that synthesizes a plain text file. 

This is authored by Jacob Bullard Computer Security Spring 2023"""


from Synthesizer import count_them_thangs

# In the beginning
what_is_this = open("cipher_text.txt", "rb") # opening for [r]eading as [b]inary
data = what_is_this.read() # if you only wanted to read 512 bytes, do .read(512)

# Between now and the beginning, I've been using StackOverFlow.
# .....and running into errors
# Let's hope this thread is actually helpful. 
# https://stackoverflow.com/questions/6787233/python-how-to-read-bytes-from-file-and-save-it

num_classification_of_thangs =len(count_them_thangs(data))
print(str(num_classification_of_thangs) + " diffrant thangs found\n")

print(count_them_thangs(data))

population_size = 0

for thang in count_them_thangs(data):
    population_size = population_size + count_them_thangs(data).get(thang)
    print("This thang: " + str(thang) + " was spotted " + str(count_them_thangs(data).get(thang)) + " particular times.")

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

# 
# Houston, we are going to need to do a little math here. 
# 
# 
