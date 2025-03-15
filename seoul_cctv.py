import pandas as pd
from tabulate import tabulate
import numpy as np

seoul_cctv_data = pd.read_excel("./data/seoul_cctv_data.xlsx") # xlsx 파일 변수에 집어넣기

seoul_cctv_data = seoul_cctv_data.drop(columns=["순번"]) # 순번칼럼 삭제
seoul_cctv_data = seoul_cctv_data.drop(index=[0]) # 총합계 열 삭제
seoul_cctv_data = seoul_cctv_data.reset_index(drop=True) # 행 삭제로 인한 행 번호 초기화

seoul_pop_data = pd.read_excel("./data/seoul_population.xlsx", header=2, usecols="B,D,G,J,N") # 구, 전체인구, 한국인, 외국인, 고령자 칼럼만 가져오기
seoul_pop_data = seoul_pop_data.rename(columns={seoul_pop_data.columns[0]:"구별",
                                                seoul_pop_data.columns[1]:"전체인구",
                                                seoul_pop_data.columns[2]:"한국인",
                                                seoul_pop_data.columns[3]:"외국인",
                                                seoul_pop_data.columns[4]:"고령자"}) # B,D,G,J,N 칼럼명 변경

seoul_cctv_data = seoul_cctv_data.replace(',','', regex=True) # 데이터 내부의 ',' (쉼표) 제거
seoul_pop_data = seoul_pop_data.replace(',','', regex=True)

seoul_cctv_data['2021년 이전'] = seoul_cctv_data.iloc[:,2:-3].sum(axis=1) # ~21년까지 설치된 cctv 합
seoul_cctv_data['2022년 이후'] = seoul_cctv_data.iloc[:,9:12].sum(axis=1) # 22~ 설치된 cctv 합
seoul_cctv_data['최근3년 증가율'] = seoul_cctv_data['2022년 이후'] / seoul_cctv_data["2021년 이전"] * 100 # 최근3년간 증가율 계산

seoul_cctv_data = seoul_cctv_data.sort_values(by='최근3년 증가율', ascending=False) # 증가율 높은 순으로 정렬



# print(tabulate(seoul_pop_data, headers="keys", tablefmt="prettry")) # tabulate로 깔끔하게 출력하기
print(tabulate(seoul_cctv_data, headers="keys", tablefmt="prettry")) 

