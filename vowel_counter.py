text = input('Text: ')
def vowel_counter(text):
    text = text.lower()
    vowels = 'aeiou'
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
   
   
    print(vowel_count)        

vowel_counter(text)
