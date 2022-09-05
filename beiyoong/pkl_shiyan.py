
import pickle
import os

savepath= 'data/clustered_random_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)
d =dict()
d["label1"]=1
d["label2"]=2
d["label3"]=3
d1 =dict()
d1["label1"]=1
d1["label2"]=2
d1["label9"]=3

data = [d,d1]
path = savepath + "shiyan.pkl"

with open(path, "wb") as f:

    pickle.dump(data, f)


my_data = pickle.load(open(path, 'rb'))
print(my_data)