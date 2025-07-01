import os
from check_h import check_hash

target = "548568964fb078e3a030da81829aa18e88f93339bd1f480fc8fa795bb6bb95b87e9661eebea26e72163063d0bda11640"

base_path = os.path.dirname(os.path.abspath(__file__))
wordlist_path = os.path.join(base_path, "wordlist.txt")

try:
    with open(wordlist_path) as f:
        for line in f:
            word = line.strip()
            if check_hash(word, target, 'sha384'):
                print("Found:", word)
                break
        else:
            print("Didn't find password.")
except FileNotFoundError:
    print(f"Didn't find wordlist.txt in file: {wordlist_path}")