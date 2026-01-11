# Create a script that takes a sentence as input and uses a 
# dictionary to count the frequency of each word. 
# The output should be the word and its count.



sentence = "the quick brown fox jumped over the lazy dog and ate and ate"

word_frequency_dictionary = {}

for word in sentence.split():
  if word in word_frequency_dictionary:
    word_frequency_dictionary[word] += 1
  else:
    word_frequency_dictionary[word] = 1

print(word_frequency_dictionary)




# Output

# {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 
# 'jumped': 1, 'over': 1, 'lazy': 1, 'dog': 1, 
# 'and': 2, 'ate': 2}