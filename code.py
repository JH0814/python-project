import csv
a = open('수산물 품목별 수출입 현황 2017년 1월.csv')
b = open('수산물 품목별 수출입 현황 2017년 2월.csv')
c = open('수산물 품목별 수출입 현황 2017년 3월.csv')
d = open('수산물 품목별 수출입 현황 2017년 4월.csv')
e = open('수산물 품목별 수출입 현황 2017년 5월.csv')
f = open('수산물 품목별 수출입 현황 2017년 6월.csv')
g = open('수산물 품목별 수출입 현황 2017년 7월.csv')
h = open('수산물 품목별 수출입 현황 2017년 8월.csv')
i = open('수산물 품목별 수출입 현황 2017년 9월.csv')
j = open('수산물 품목별 수출입 현황 2017년 10월.csv')
k = open('수산물 품목별 수출입 현황 2017년 11월.csv')
l = open('수산물 품목별 수출입 현황 2017년 12월.csv')

r = input('어떤 종류의 품목을 알고싶으신가요?')
s = input('어떤 상태를 알고 싶으신가요?')
x = []
a2 = csv.reader(a)
a = next(a)
for row in a2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
        t = row[3]
b2 = csv.reader(b)
b = next(b)
for row in b2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
c2 = csv.reader(c)
c = next(c)
for row in c2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
d2 = csv.reader(d)
d = next(d)
for row in d2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
e2 = csv.reader(e)
e = next(e)
for row in e2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
f2 = csv.reader(f)
f = next(f)
for row in f2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
g2 = csv.reader(g)
g = next(g)
for row in g2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
h2 = csv.reader(h)
h = next(h)
for row in h2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
i2 = csv.reader(i)
i = next(i)
for row in i2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
j2 = csv.reader(j)
j = next(j)
for row in j2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
k2 = csv.reader(k)
k = next(k)
for row in k2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
l2 = csv.reader(l)
l = next(l)
for row in l2 :
    if r in row[3] and s in row[3] and row[4] == '수출' :
        x.append(int(row[5]))
import matplotlib.pyplot as plt
data = x
plt.bar(range(len(data)), data)
plt.rc('font', family='Malgun Gothic')
plt.title('월별 ' + t + '수출량')
plt.xticks(range(12),['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'], rotation=90)
plt.xlabel('월')
plt.ylabel('수출 중량')
plt.show()
