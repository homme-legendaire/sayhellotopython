import numpy as np

coffee = [87, 63, 64, 110, 144, 143, 69, 53, 133, 55, 78, 123, 63, 101]
waffle = [87, 36, 32, 101, 41, 78, 115, 31, 53, 11, 13, 119, 25, 65]

coffee = np.array(coffee)*3400
waffle = np.array(waffle)*6700

print(coffee)
print(waffle)

coffee_total = np.sum(coffee)
waffle_total = np.sum(waffle)
coffee_avg = int(coffee_total/len(coffee))
waffle_avg = int(waffle_total/len(waffle))
print(f"커피의 총 매출은: {coffee_total}원 입니다.")
print(f"와플의 총 매출은: {waffle_total}원 입니다.")
print(f"커피의 평균 매출은 : {coffee_avg}원 입니다.")
print(f"와플의 평균 매출은 : {waffle_avg}원 입니다.")

total = coffee+waffle
print(total)

Filter = np.where(total <= 450000)
print(Filter)
print(total[Filter])
