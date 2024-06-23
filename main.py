from CosineSimilarity import CosineSimilarity
import os
fileFolder = 'QueryText/'
def get_query_file(filename):    
    f = open(fileFolder + filename, 'r', errors="ignore")
    text = f.read()
    text = text.lower()
    f.close()
    return text

if __name__ == '__main__':
    query_file_name = input("Enter your query file: ")
    exist = os.path.exists(fileFolder+query_file_name)
    if exist:
        query = get_query_file(query_file_name)
        cs = CosineSimilarity(query)
        # print("QUERY 1 : ", query)
        print("Top 1: ", cs.get_similar_documents()[0])
        print("Top 2: ", cs.get_similar_documents()[1])
        print("Top 3: ", cs.get_similar_documents()[2])
    else:
        print("Check the format or check the correct file name.")
