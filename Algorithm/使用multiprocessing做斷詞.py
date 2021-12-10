# json url -> https://drive.google.com/drive/folders/1qbrEcaN021pxxaLSk4hMrUTBEIaeUJAM?usp=sharing

from multiprocessing import Pool
import pandas as pd
import jieba
import jieba.analyse
import time
df=pd.read_json('./test_not_send/book_intro_clean_jieba.json',lines=True) #讀取json
jieba.set_dictionary('test_not_send/dict.txt.big') # 讀取jieba 辭庫

df_store=df.to_dict('record') # pandas 轉dict ->會先變 list
need=df_store[:200000] # list前 200000筆 (做分段)

def cut_word(dict1):
    cw=jieba.cut(dict1['words']) # 斷字 -> iterable (list)
    result=' '.join(cw) # 換成字串
    tags=jieba.analyse.extract_tags(result,topK=40,allowPOS=('n','ns','nz','v')) # top10 詞 -> list
    dict1['jieba_cut']=','.join(tags) # 換成字串 
    del dict1['words'] #把Key為words刪除(刪除column) 
    return dict1 # 回傳
if __name__ == '__main__':
    start_time=time.time()
    with Pool(8) as p: # 8 cpu
        need1=p.map(cut_word,need) # 做上方function
    end_time=time.time()
    print(end_time-start_time) # 比較時間
    df_need=pd.DataFrame(need1) #轉成dataframe
    df_need.to_json('df_need1.json',orient='records',lines=True,force_ascii=False)
    
