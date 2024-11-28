def solution(id_list, report, k):
    # 1. 중복 신고 제거
    report = list(set(report))  # 중복 신고 제거

    # 2. 신고당한 횟수 계산
    report_count = {user: 0 for user in id_list}  # 각 유저별 신고당한 횟수 초기화
    report_info = {user: [] for user in id_list}  # 각 유저가 신고한 대상 초기화

    for r in report:
        reporter, reported = r.split()  # 신고자와 신고 대상 분리
        report_info[reporter].append(reported)  # 신고자가 신고한 대상 기록
        report_count[reported] += 1  # 신고 횟수 증가

    # 3. 정지된 유저 판별
    suspended_users = {user for user, count in report_count.items() if count >= k}

    # 4. 결과 메일 수 계산
    result = []
    for user in id_list:
        mail_count = sum(1 for reported in report_info[user] if reported in suspended_users)
        result.append(mail_count)

    return result
