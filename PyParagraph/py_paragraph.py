import os
import re


with open('paragraph_1.txt') as text:
    paragraph = text.read().replace('\n', ' ')

# count the words
# split the paragraph base on space
word_split = paragraph.split(" ")
word_count = len(word_split)

# letter count per word
letter_count = []
for word in word_split:
    letter_count.append(len(word))
#[letter_count.append(len(word)) for word in word_split]

# avarage letter count
avg_letter_count = sum(letter_count) / len(letter_count)

# pereform sentence split by splitting the paragraph based on punctuation
sentence_split = re.split("(?<=[.!?]) +", paragraph)
sentence_len = len(sentence_split)
#print(sentence_split)

# calculate the number of word in each sentence
word_per_sent = []
for sentence in sentence_split:
    word_per_sent.append(len(sentence.split(' ')))

# avarage word count per sentence
avg_sent_count = sum(word_per_sent)/len(word_per_sent)


# save and print the output
output = os.path.join('output.txt')
with open(output, 'w') as result:
    result.write(f"\nParagraph Analysis\n")
    result.write(f"-----------------\n")
    result.write(f"Approximate Word Count: {word_count}\n")
    result.write(f"Approximate Sentence Count: {sentence_len}\n")
    result.write(f"Average Letter Count: {round(avg_letter_count, 0)}\n")
    result.write(f"Average Sentence Length: {round(avg_sent_count,0)}\n")

# Print all of the results (to terminal)
print(output)

with open(output, 'r') as readfile:
    print(readfile.read())