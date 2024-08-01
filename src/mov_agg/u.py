import pandas as pd

def merge(load_dt="20240724"):
    read_df = pd.read_parquet('~/tmp/test_parquet2')
    cols = ['movieCd', #영화의 대표코드를 출력합니다.
       'movieNm', #영화명(국문)을 출력합니다.
        #'openDt', #영화의 개봉일을 출력합니다.
        #'audiCnt', #해당일의 관객수를 출력합니다.
        'load_dt', # 입수일자
        'multiMovieYn', #다양성영화 유무
        'repNationCd', #한국외국영화 유무
       ]
    
    df = read_df[cols]
    #print(df.head(5))
    #울버린만 조회
    #df_where = df[df['movieCd']=='20247781'].copy()
    df_where = df[(df['movieCd']=='20247781') & (df['load_dt']==int(load_dt))].copy()
    print(df_where)

    #카테고리 타입->Object
    df_where['load_dt']= df_where['load_dt'].astype('object')
    df_where['multiMovieYn'] = df_where['multiMovieYn'].astype('object')
    df_where['multiMovieYn'] = df_where['multiMovieYn'].astype('object')
    print(df_where.dtypes)
    
    return df_where

merge()
