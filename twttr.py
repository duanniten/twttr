def main():
    text = input("Input: ")
    
    vowels = [
            'A', 'a',
            'E', 'e',
            'I', 'i',
            'O', 'o', 
            'U', 'u'
            ]
    
    new_text = ""
    for lether in text:
        if lether not in vowels:
            new_text += lether

    print("Output:", new_text)

main()