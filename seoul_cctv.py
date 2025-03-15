import pandas as pd
from tabulate import tabulate

seoul_cctv_data = pd.read_excel("/home/sch/dev_ws/EDA/seoul_cctv/data/seoul_cctv_data.xlsx") # xlsx 파일 변수에 집어넣기
print(tabulate(seoul_cctv_data, headers="keys", tablefmt="prettry")) #tabulate로 깔끔하게 출력하기