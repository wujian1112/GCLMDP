
import pickle
import os

savepath= 'data/clustered_random_graph/'
a= os.path.exists(savepath)
if not a:
    os.makedirs(savepath)

data = ["label1", "label2", "label3", "label4", "label_i"]
path = savepath + "shiyan.pkl"
with open(path, "ab+") as f:
    for d in data:
        pickle.dump(d, f)


my_data = pickle.load(open(path, 'rb'))
print(my_data)