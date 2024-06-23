# calculate cosine similarity between query and document
import math
from tfidf import tfidf
from PreprocessQuery import PreprocessQuery
from PostingList import PostingList

class CosineSimilarity:
    def __init__(self, query):
        self.tf_idf = tfidf()
        self.tf_idf.get_tfidf_weights()
        self.tfidf = self.tf_idf.tfidf_wts
        self.query = query
        self.preprocess_query = PreprocessQuery(self.query)
        self.preprocessed_query = self.preprocess_query.get_preprocessed_query()
        self.query_tfidf = self.tf_idf.query_tfidf(self.preprocessed_query)
        self.N = self.tf_idf.get_N()
        pl = PostingList()
        self.file_index = pl.get_file_index()
        # print("File Index: ", self.file_index)
        # print(self.N)

    def euclidean_length(self, vector):
        return math.sqrt(sum(i*i for i in vector))


    def cosine_similarity(self, query, doc):
        sum = 0
        query_scores = []
        for key in query:
            query_scores.append(query[key])
        for i in range(len(query)):
            sum += query_scores[i] * doc[i]
        sum /= self.euclidean_length(doc)*self.euclidean_length(query_scores)
        return sum
    
    def get_all_docs(self):
        self.possible_relevant_docs = {}
        i = int(0)
        for q in self.preprocessed_query:
            if q in self.tfidf:
                dic = self.tfidf[q][1]
                for key in dic:
                    if key in self.possible_relevant_docs:
                        self.possible_relevant_docs[key][i] = dic[key]
                    else:
                        self.possible_relevant_docs[key] = [0] * len(self.preprocessed_query)
                        self.possible_relevant_docs[key][i] = dic[key]                
            # print(self.possible_relevant_docs)
            i += 1  
        
        
    
    def get_similar_documents(self, n=3):
        self.get_all_docs()
        self.similar_documents = {}
        for doc in self.possible_relevant_docs:
            self.similar_documents[doc] = self.cosine_similarity(self.query_tfidf, self.possible_relevant_docs[doc])
        self.similar_documents = sorted(self.similar_documents.items(), key=lambda x: x[1], reverse=True)
        doc_name = []
        for key in self.similar_documents:
            doc_name.append(self.file_index[key[0]])
        if len(doc_name) < n:
            return doc_name
        return doc_name[:n]
    

if __name__ == '__main__':
    query = 'Ta'
    print("Query = ", query)
    cosine_similarity = CosineSimilarity(query)
    print(cosine_similarity.get_similar_documents())