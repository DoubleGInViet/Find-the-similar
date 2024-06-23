def get_query_file(filename):
    fileFolder = 'QueryText/'
    f = open(fileFolder + filename, 'r', errors="ignore")
    text = f.read()
    text = text.lower()
    f.close()
    return text

if __name__== '__main__':
    print(get_query_file('a1.txt'))
