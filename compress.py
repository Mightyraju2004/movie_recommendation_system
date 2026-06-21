import gzip
import pickle

print("Fast compression (gzip) shuru ho rahi hai...")

# 1. Purani similarity file load karein
similarity = pickle.load(open("similarity.pkl", "rb"))

# 2. Gzip ke sath compress karein (Yeh loading me bohot fast hai)
with gzip.open("similarity_fast.gzip", "wb") as f:
    pickle.dump(similarity, f)

print("Mubarak ho! 'similarity_fast.gzip' ban gayi hai.")