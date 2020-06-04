def isogram(string):
    if isinstance(string,str) and len(string)!=0 :
        string1=string.lower()
        return string, len(string1)==len(set(string1))
    if not string:
        return string, False

print(isogram('prak'))
