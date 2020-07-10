import numpy as np
from sentence_transformers import SentenceTransformer
import ngtpy


class Classificator():
    def __init__(self, path: str = '/app/model_weight/model_weight'):
        self.model = SentenceTransformer(path)
        X = np.load('/app/newsgroup_data_encoded/X_train_encoded.npy')
        self.y = np.load('/app/newsgroup_data_encoded/y_train.npy')
        self.index = self.create_index(X)


    def create_index(self, X):
        dim = len(X[0])
        ngtpy.create(b'Index', dim)
        index = ngtpy.Index(b'Index')
        index.batch_insert(X)
        index.save()
        return index


    def classify(self, query: str, size_k: int=9) -> (str, str):
        vote_array = np.zeros(20)
        query = self.model.encode(query)
        query_res = self.index.search(query, size=size_k)
        for neighbor in query_res:
            if neighbor[1] == 0:
                vote_array[self.y[int(neighbor[0])]] = 1
                break
            vote_array[self.y[int(neighbor[0])]] = 1 / neighbor[1]
        res = np.argmax(vote_array)
        return str(res), labels[int(res)]



labels = ['alt.atheism',
          'comp.graphics',
          'comp.os.ms-windows.misc',
          'comp.sys.ibm.pc.hardware',
          'comp.sys.mac.hardware',
          'comp.windows.x',
          'misc.forsale',
          'rec.autos',
          'rec.motorcycles',
          'rec.sport.baseball',
          'rec.sport.hockey',
          'sci.crypt',
          'sci.electronics',
          'sci.med',
          'sci.space',
          'soc.religion.christian',
          'talk.politics.guns',
          'talk.politics.mideast',
          'talk.politics.misc',
          'talk.religion.misc']
