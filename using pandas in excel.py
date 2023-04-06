import numpy as np
import pandas as pd

scores_df = pd.read_excel('sample_scores.xlsx')
#print(scores_df)
scores_df['average'] = scores_df.mean(axis=1)

scores_df['pass/fail'] = np.where(scores_df['average'] > 60,'pass', 'fail')
#print(scores_df)

scores_df['pass/fail'] = ['pass' if x > 60 else 'fail' for x in scores_df['average'] ]
#print(scores_df)
