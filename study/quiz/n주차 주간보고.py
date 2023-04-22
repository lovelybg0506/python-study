# 퀴즈 ) 당신의 회사에서는 매주1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 - 
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차 부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

# 이것도되는데 아래에서 쓴 with open이 더 간결하긴함
for n in range(1,51):
    filename = "{0}주차.txt".format(n)
    week_report = open(filename, "w", encoding="utf8") # w = write 쓰기용도
    print("- {0} 주차 주간보고 -".format(n), file=week_report)
    print("부서 : ", file=week_report)
    print("이름 : ", file=week_report)
    print("업무 요약 : ", file=week_report)
    week_report.close()

# 정답
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")