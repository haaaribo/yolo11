from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)

PYTHON_CODE = '''
import pandas as pd
import numpy as np
import datetime


path = '20230303084334_KF008102_sensorData.csv'


df_result = f_read_emotion_csv_20230923(path, jeouls='all')


df_result.loc[df_result['j01'] <= 30, 'j01'] = np.nan
df_result.loc[df_result['j02'] <= 30, 'j02'] = np.nan
df_result.loc[df_result['j03'] <= 30, 'j03'] = np.nan


df_result
'''

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=100, chunk_overlap=0
)

python_docs = python_splitter.create_documents([PYTHON_CODE])
python_docs

for doc in python_docs:
    print(doc.page_content, end="\n==================\n")