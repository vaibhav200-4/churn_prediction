import pickle

with open('one_hot_encoder.pkl', 'rb') as f:
    one_hot_encoder = pickle.load(f)

print(one_hot_encoder)
print(one_hot_encoder.categories_)
print(one_hot_encoder.categories_[0])
print(one_hot_encoder.get_feature_names_out())