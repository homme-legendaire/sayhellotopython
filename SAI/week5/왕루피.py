from datetime import *  # 살아온 날 계산
import pandas as pd
df = pd.read_excel('1급기밀-뽀국민 사찰 자료.xlsx')  # 엑셀파일 불러오기
df = df.drop_duplicates(['이름'])  # 중복 제거
kill = df[(df['평균 답장 시간(분)'] > df['평균 답장 시간(분)'].mean())
          & (df['좋아하는 아이돌'] != '빅뱅')]  # 범죄자 색출 (빅뱅팬 제외)
year, month, day = map(int, input('오늘 날짜를 입력해주세요:').split('.'))
today = date(year, month, day)


def count_days(day):
    y, m, d = map(int, day.split('.'))
    lifetime = date(y, m, d)
    return (today-lifetime).days


kill['일생'] = kill['생년월일'].map(count_days)
kill = kill.sort_values(by='평균 답장 시간(분)')  # 답장 시간 순으로 정렬
kill.reset_index(drop=True, inplace=True)  # 인덱스 초기화
young = []  # 촉법소년
cnt = 1
for row in kill['일생']:
    if row >= 3000:
        young.append(f'징역 {cnt}년형')
        cnt += 1
    else:
        young.append('촉법소년')
kill['형량'] = young
kill = kill.drop(['일생'], axis=1)
kill.to_excel('범죄자 명단.xlsx')
