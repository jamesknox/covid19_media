import pickle

infile = open('min_df_10/bow_va_sources.pkl','rb')
new_dict = pickle.load(infile)
print(new_dict)
infile.close()