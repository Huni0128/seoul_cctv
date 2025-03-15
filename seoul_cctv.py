import pandas as pd
from tabulate import tabulate
import numpy as np

def seoul_population():
    seoul_pop_data = pd.read_excel("./data/seoul_population.xlsx", header=2, usecols="B,D,G,J,N") # 구, 전체인구, 한국인, 외국인, 고령자 칼럼만 가져오기
    seoul_pop_data = seoul_pop_data.rename(columns={seoul_pop_data.columns[0]:"구별",
                                                    seoul_pop_data.columns[1]:"전체인구",
                                                    seoul_pop_data.columns[2]:"한국인",
                                                    seoul_pop_data.columns[3]:"외국인",
                                                    seoul_pop_data.columns[4]:"고령자"}) # B,D,G,J,N 칼럼명 변경

    seoul_pop_data = seoul_pop_data.replace(',','', regex=True) # 데이터 내부의 ',' (쉼표) 제거
    seoul_pop_data = seoul_pop_data.replace(' ','', regex=True) # 데이터 내부의 공백 제거
    seoul_pop_data = seoul_pop_data.drop(index=[0]) # 총합계 열 삭제
    
    seoul_pop_data["외국인비율"] = seoul_pop_data["외국인"] / seoul_pop_data["전체인구"] * 100
    seoul_pop_data["고령자비율"] = seoul_pop_data["고령자"] / seoul_pop_data["전체인구"] * 100
    
    return seoul_pop_data


def seoul_cctv():
    
    seoul_cctv_data = pd.read_excel("./data/seoul_cctv_data.xlsx") # xlsx 파일 변수에 집어넣기

    seoul_cctv_data = seoul_cctv_data.drop(columns=["순번"]) # 순번칼럼 삭제
    seoul_cctv_data = seoul_cctv_data.drop(index=[0]) # 총합계 열 삭제
    seoul_cctv_data = seoul_cctv_data.reset_index(drop=True) # 행 삭제로 인한 행 번호 초기화
    seoul_cctv_data = seoul_cctv_data.replace(',','', regex=True) # 데이터 내부의 ',' (쉼표) 제거
    seoul_cctv_data = seoul_cctv_data.replace(' ','', regex=True) # 데이터 내부의 공백 제거
    seoul_cctv_data = seoul_cctv_data.rename(columns={"구분":"구별"})
    
    seoul_cctv_data['2021년 이전'] = seoul_cctv_data.iloc[:,2:-3].sum(axis=1)
    seoul_cctv_data['2022년 이후'] = seoul_cctv_data.iloc[:,9:12].sum(axis=1)
    seoul_cctv_data['최근3년 증가율'] = seoul_cctv_data['2022년 이후'] / seoul_cctv_data["2021년 이전"] * 100
    
    seoul_cctv_data = seoul_cctv_data.sort_values(by='최근3년 증가율', ascending=False) # 증가율 높은 순으로 정렬
    
    return seoul_cctv_data
    
seoul_merge = pd.merge(seoul_cctv(),seoul_population(), on='구별', how="left")

print(tabulate(seoul_merge, headers="keys", tablefmt="prettry"))

