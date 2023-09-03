def capitalize_words(input_string):
    words = input_string.split()  
    capitalized_words = []

    for word in words:
        if len(word) > 0:
            first_char = word[0]

           
            if 'a' <= first_char <= 'z':
               
                first_char = chr(ord(first_char) - 32)

            capitalized_word = first_char + word[1:]  
            capitalized_words.append(capitalized_word)
        else:
            capitalized_words.append("")  

    
    return ' '.join(capitalized_words)


input_string = "hello world , sdd ARkk  rqwerty A   qwe"

print(capitalize_words(input_string))  
