import pandas as pd
from tabulate import tabulate

seoul_cctv_data = pd.read_excel("./data/seoul_cctv_data.xlsx") # xlsx 파일 변수에 집어넣기

seoul_cctv_data = seoul_cctv_data.drop(columns=["순번"]) # 순번칼럼 삭제
seoul_cctv_data = seoul_cctv_data.drop(index=[0]) # 총합계 열 삭제
seoul_cctv_data = seoul_cctv_data.reset_index(drop=True) # 행 삭제로 인한 행 번호 초기화

seoul_pop_data = pd.read_excel("./data/seoul_population.xlsx", header=2, usecols="B,D,G,J,N") # 구, 전체인구, 한국인, 외국인, 고령자 칼럼만 가져오기
seoul_pop_data = seoul_pop_data.rename(columns={seoul_pop_data.columns[0]:"구별",
                                                seoul_pop_data.columns[1]:"전체인구",
                                                seoul_pop_data.columns[2]:"한국인",
                                                seoul_pop_data.columns[3]:"외국인",
                                                seoul_pop_data.columns[4]:"고령자"})

print(tabulate(seoul_pop_data, headers="keys", tablefmt="prettry")) # tabulate로 깔끔하게 출력하기
# print(tabulate(seoul_cctv_data, headers="keys", tablefmt="prettry")) 

