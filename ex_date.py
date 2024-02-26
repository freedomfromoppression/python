import datetime
# 현재 날짜와 시간
now = datetime.datetime.now()
print(now)
#특정 날짜와 시간
dt = datetime.datetime(2024,2,19,12,30)
print(dt)
#오늘 날짜
today = datetime.date.today()
print(today)
# 날짜와 시간을 문자열로 반환(포멧)
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
#문자를 날짜로
str_to_dr = datetime.datetime.strptime("2024-02-18", "%Y-%m-%d")
print(str_to_dr)

st_date =datetime.date(2024, 1, 1)
end_date = datetime.date(2024,2, 20)
dalta = end_date - st_date
print(dalta)
weekday = end_date.weekday()# 월:0. 화:1.......
print("요일:", weekday)
import calendar
year = 2024
month = 2
first_weekday, num_days = calendar.monthrange(2024, 2)
# print(first_weekday, num_days)
print(f"{year}년 {month}월")
print("월 화 수 목 금 토 일")
#첫쨰 날 시작 요일까지 공백으로
print("   "*first_weekday, end="")
#1일 부터 마지막날까지 출력
for day in range(1, num_days + 1):
    print(f"{day:2}", end=" ") #{day:2} <-- 2자리 차지하도록
    first_weekday += 1
    if first_weekday == 7: #요일의 마지막 새로운줄로
        print()
        first_weekday = 0
