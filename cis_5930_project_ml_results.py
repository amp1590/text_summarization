# -*- coding: utf-8 -*-
"""CIS 5930 Project: ML Results.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kH9tkj2JAxg-XLXAPQ7No9-Jv31mibIP

# Machine Learning Results

## Connect to GoogleDrive
"""

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab\ Notebooks/CIS5930_Project/
# %ls

"""## Section 1: Supervised Learning Using Only Embedding Information

### LogReg Embedding Only
"""

import pandas as pd

#load results data
input_default =  'cv_results_top_3_logreg_default.pickle'
r_def = pd.read_pickle(input_default)

#wrap rouge score in dataframe
df_def = pd.DataFrame(r_def['Rouge']['rouge1'], index=['LogisticReg']).apply(lambda x: round(x,3))
df_logreg = pd.concat([df_def])
df_logreg.columns.name = 'ROUGE-1'
#df_logreg.index.name = 'LogisticReg'
df_logreg[['f1', 'recall', 'precision']]

"""### Neural Nets"""

#load results
#load results
input_2525 = 'cv_results_nn2525_embeddings_only_cw_top3_epochs50.pickle'
input_2550 = 'cv_results_nn2550_embeddings_only_cw_top3_epochs50.pickle'
input_5050 = 'cv_results_nn5050_embeddings_only_cw_top3_epochs50.pickle'

r_nn2525 = pd.read_pickle(input_2525)
r_nn2550 = pd.read_pickle(input_2550)
r_nn5050 = pd.read_pickle(input_5050)

#wrap rouge score in dataframe
df_nn2525 = pd.DataFrame(r_nn2525['Rouge']['rouge1'], index=['NN 25 25']).apply(lambda x: round(x,3))
df_nn2550 = pd.DataFrame(r_nn2550['Rouge']['rouge1'], index=['NN 25 50']).apply(lambda x: round(x,3))
df_nn5050 = pd.DataFrame(r_nn5050['Rouge']['rouge1'], index=['NN 50 50']).apply(lambda x: round(x,3))

#concatenate
df_nn = pd.concat([df_nn2525, df_nn2550, df_nn5050])

#display
df_nn.columns.name = 'ROUGE-1'
df_nn.index.name = 'Neural Network (Dense Dense)'
df_nn = df_nn[['f1', 'recall', 'precision']]

df_nn

"""## Score comparison between Logistic Regresseion and Neural Net"""

input_default = 'cv_results_top_3_logreg_default.pickle'
input_5050 = 'cv_results_nn5050_embeddings_only_cw_top3_epochs50.pickle'
r_def = pd.read_pickle(input_default)
r_nn5050 = pd.read_pickle(input_5050)

#wrap rouge score in dataframe
df_def = pd.DataFrame(r_def['Rouge']['rouge1'], index=['Logistic Reg']).apply(lambda x: round(x,3))
df_nn5050 = pd.DataFrame(r_nn5050['Rouge']['rouge1'], index=['NN 50 50']).apply(lambda x: round(x,3))

#concatenate
df_nn = pd.concat([df_def, df_nn5050])

#display
df_nn.columns.name = 'ROUGE-1'
#df_nn.index.name = 'Neural Network (Dense Dense)'
df_nn = df_nn[['f1', 'recall', 'precision']]

df_nn

"""## Section 2: Supervised Learning Including Sequential Information

### LogReg with Sentence Number
"""

#load data
import pandas as pd

input_sent_num_def =  'cv_results_top_3_logreg_sent_num_no_bal.pickle'
#input_sent_num_bal = 'cv_results_top_3_logreg_sent_num_bal.pickle'

r_sent_num_def = pd.read_pickle(input_sent_num_def)
#r_sent_num_bal = pd.read_pickle(input_sent_num_bal)

#wrap rouge score in dataframe, concatenate and display
df_sent_num_def= pd.DataFrame(r_sent_num_def['Rouge']['rouge1'], index=['Logistic Reg']).apply(lambda x: round(x,3))
#df_sent_num_bal = pd.DataFrame(r_sent_num_bal['Rouge']['rouge1'], index=['Balanced']).apply(lambda x: round(x,3))

df_lr_sent_num = pd.concat([df_sent_num_def]) 
df_lr_sent_num.columns.name = 'ROUGE-1'
#df_lr_sent_num.index.name = 'LogReg'
df_lr_sent_num[['f1', 'recall', 'precision']]

"""### Long Short Term Memory (LSTM)"""

#load data
input_lstm_un25 = 'cv_results_lstm_uni25_embeddings_only_epochs1_top3.pickle'
input_lstm_un50 = 'cv_results_lstm_uni50_embeddings_only_epochs1_top3.pickle'
input_lstm_bi25 = 'cv_results_lstm_bi25_embeddings_only_epochs1_top3.pickle'
input_lstm_bi50 = 'cv_results_lstm_bi50_embeddings_only_epochs1_top3.pickle'
input_lstm_bi75 = 'cv_results_lstm_bi75_embeddings_only_epochs1_top3.pickle'

r_lstm_un25 = pd.read_pickle(input_lstm_un25)
r_lstm_un50 = pd.read_pickle(input_lstm_un50)
r_lstm_bi25 = pd.read_pickle(input_lstm_bi25)
r_lstm_bi50 = pd.read_pickle(input_lstm_bi50)
r_lstm_bi50 = pd.read_pickle(input_lstm_bi75)

#wrap rouge score in dataframe

df_lstm_un25 = pd.DataFrame(r_lstm_un25['Rouge']['rouge1'], index=['LSTM Uni 25']).apply(lambda x: round(x,3))
df_lstm_un50 = pd.DataFrame(r_lstm_un50['Rouge']['rouge1'], index=['LSTM Uni 50']).apply(lambda x: round(x,3))
df_lstm_bi25 = pd.DataFrame(r_lstm_bi25['Rouge']['rouge1'], index=['LSTM Bi 25']).apply(lambda x: round(x,3))
df_lstm_bi50 = pd.DataFrame(r_lstm_bi50['Rouge']['rouge1'], index=['LSTM Bi 50']).apply(lambda x: round(x,3))
df_lstm_bi75 = pd.DataFrame(r_lstm_bi50['Rouge']['rouge1'], index=['LSTM Bi 75']).apply(lambda x: round(x,3))

#concatenate
df_lstm = pd.concat([df_lstm_un25, df_lstm_un50, df_lstm_bi25, df_lstm_bi50, df_lstm_bi75])

#display Rouge1
df_lstm.columns.name = 'ROUGE-1'
df_lstm.index.name = 'LSTM'
df_lstm = df_lstm[['f1', 'recall', 'precision']]

df_lstm

"""### LEDE3

### Rouge1
"""

#load data
input_lede3 = 'cv_results_LEDE3.pickle'
r_lede3 = pd.read_pickle(input_lede3)
df_lede3 = pd.DataFrame(r_lede3['Rouge']['rouge1'], index=['LEDE3']).apply(lambda x: round(x,3))

#concatenate optimal models for baseline comparison and display Rouge1
df_lede3_comp = pd.concat([df_lede3, df_sent_num_def, df_lstm_bi50])
df_lede3_comp=df_lede3_comp[['f1', 'recall', 'precision']]
df_lede3_comp.index = ['LEDE3', 'Logistic Reg', 'LSTM Bi 50']
df_lede3_comp.columns.name = 'ROUGE-1'
df_lede3_comp

"""### Load TextRank Data"""

#load results
input_textrank = 'cv_results_textrank.pickle'
r_textrank = pd.read_pickle(input_textrank)

for key, value in r_textrank.items():
  print(key)

df =  r_textrank['df_original']

df.loc[8]['summary']

summaries = r_textrank['summaries_comp']

"""###Pull article and display summaries across models + gold summary

"""

#Pull article and display summaries across models + gold summary
article_label = 1

print('\033[1m{:10s}\033[0m'.format('Original')) 
print(r_textrank['summaries_comp'][article_label][1].replace('\n\n', ''))
print('')

print('\033[1m{:10s}\033[0m'.format('Logistic Reg')) 
print(r_def['summaries_comp'][article_label][0].replace('\n\n', ''))
print('')

print('\033[1m{:10s}\033[0m'.format('Neural Net')) 
print(r_nn2525['summaries_comp'][article_label][0].replace('\n\n', ''))
print('')

print('\033[1m{:10s}\033[0m'.format('LSTM')) 
print(r_lstm_bi50['summaries_comp'][article_label][0].replace('\n\n', ''))
print('')

print('\033[1m{:10s}\033[0m'.format('LEDE3')) 
print(r_lede3['summaries_comp'][article_label][0].replace('\n\n', ''))
print('')


#print('\033[1m{:10s}\033[0m'.format('TextRank')) 
#print(r_textrank['summaries_comp'][article_label][0].replace('\n\n', ''))

# TESTTT LIZA READ PICKLE FILE
input_file = 'cv_results_top_3_logreg_default.pickle'
r_test_pickle = pd.read_pickle(input_file)