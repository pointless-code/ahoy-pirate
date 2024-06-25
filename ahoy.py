import sys
from ahoy_dictionary import ahoy_dictionary

def translate_to_pirate(text):
    words = text.split()
    pirate_text = " ".join([ahoy_dictionary.get(word.lower(), word) for word in words])
    return pirate_text

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ahoy.py '<text>'")
        sys.exit(1)
    
    text = " ".join(sys.argv[1:])
    translated_text = translate_to_pirate(text)
    print(translated_text)
