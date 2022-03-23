import pandas as pd
df = pd.read_csv('./data/friend_list.csv')
print(df)  # 전체 엑셀값 출력
print(df.head(2))  # 위에서부터 n행 출력
print(df.tail(3))  # 밑에서부터 n행 출력

df = pd.read_csv('./data/friend_list.txt')  # txt 파일 불러오기
print(df)

df = pd.read_csv('./data/friend_list_tab.txt')  # ,가 아닌 탭으로 구별되어 있는 문서
print(df)

df = pd.read_csv('./data/friend_list_tab.txt',
                 delimiter='\t')  # delimiter를 추가해줘야함
print(df)

df = pd.read_csv('./data/friend_list_no_head.csv', header=None)  # 헤더가 없는 파일
print(df)
df.columns = ['name', 'age', 'job']  # 열 이름 추가
print(df)

df = pd.read_csv('./data/friend_list_no_head.csv', header=None,
                 names=['name', 'age', 'job'])  # 위 과정을 한 번에
print(df)
