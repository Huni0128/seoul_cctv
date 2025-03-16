# 서울시 CCTV 데이터 분석

이 프로젝트는 서울시 각 구별 CCTV 설치 현황과 인구 데이터를 분석하여, CCTV 설치 비율과 인구수 간의 관계를 탐구합니다.

## 📁 데이터

- **CCTV 데이터**: 서울시 각 구별 CCTV 설치 현황
- **인구 데이터**: 서울시 각 구별 인구수 및 기타 인구 통계

## 📂 데이터 출처
- [서울시 CCTV 데이터](https://data.seoul.go.kr/dataList/OA-2734/F/1/datasetView.do)
- [서울시 인구 데이터](https://data.seoul.go.kr/dataList/419/S/2/datasetView.do)

## 🛠 STACK
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![VS Code](https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) 

![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

## 📊 분석 내용

- **CCTV 설치 현황**: 각 구별 CCTV 설치 대수 및 비율 분석
- **인구 대비 CCTV 비율**: 인구수 대비 CCTV 설치 비율 계산
- **시각화**: 산점도 및 경향선(Trend Line)을 활용한 데이터 시각화

## 📊 분석 결과 예제
![구별 CCTV 데이터 시각화](images/CCTV_graph.png)

![인구수에 따른 CCTV 개수 ](images/CCTV_plot.png)

## 🔍 주요 분석 결과
- CCTV 개수는 인구수와 강한 상관관계를 가지지 않음.
- 강남구, 관악구 등 특정 지역에 CCTV가 집중되어 있음.
- 송파구, 강서구 등 인구 밀도가 높은 지역 중 일부는 CCTV가 상대적으로 부족함.

## 📌 개선점 및 아쉬운 점
이 프로젝트를 진행하면서 다음과 같은 어려움이 있었으며 향후 개선할 수 있는 부분을 정리합니다.

### **1️.Pandas 데이터프레임 인덱스 문제**
- `set_index("구별")`을 사용할 때 `inplace=True`를 사용하면 데이터가 `None`이 되는 문제가 발생했습니다.  
- **해결:** `inplace=True`를 제거하고, `seoul_data = seoul_data.set_index("구별")`로 수정하여 정상적으로 동작하도록 개선했습니다.  

### **2️.그래프 시각화 개선**
- `seaborn` 대신 `matplotlib`을 사용하면서 `scatter()` 및 `plot()`을 수동으로 설정해야 하는 어려움이 있었습니다.  
- **해결:** `np.polyfit()`과 `np.poly1d()`를 활용하여 경향선을 직접 계산하고 추가하였습니다.  

### **3️.Scatter Plot에서 구별 이름 표시 문제**
- `plt.text()`와 `plt.annotate()`를 사용하여 각 점에 구 이름을 표시했지만, 일부 텍스트가 겹치는 문제가 발생했습니다.  
- **해결:** `xytext=(-10,5)` 등의 옵션을 활용하여 텍스트 위치를 조정하여 가독성을 개선했습니다.  

### **4️.GitHub README 및 이미지 삽입 문제**
- GitHub Issue에 업로드한 이미지를 README.md에서 불러오면 깨지는 경우가 있었습니다.  
- **해결:** 저장소에 `/images` 폴더를 만들어 직접 이미지 파일을 업로드한 후, 상대 경로를 사용하여 이미지를 삽입하였습니다.  

### **5️.Git Push 오류 (`fetch first` 문제)**
- 원격 저장소와 로컬 브랜치가 동기화되지 않아 `git push`가 거부되는 문제가 발생했습니다.  
- **해결:** `git pull origin main --rebase` 명령어를 사용하여 원격 저장소와 동기화한 후, `git push origin main`을 실행하여 정상적으로 반영했습니다.  




