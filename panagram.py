def panagram(string):
    alphabet='abcdefghijklmnopqurstuvwxyz'
    for char in alphabet:
        if char not in string.lower():
            return False
    return True

string="the quick brown fox jumps over the lazy dog"
print(panagram(string))