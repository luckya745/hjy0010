import re

filename = r'c:\Users\User\Downloads\history_aiedu_app\tabs\ch4_full.md'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

target = """평가 요소
(배점)
점수
채점 기준
인물의 
생애주기
별 
겪었을 
주요 사건 
관련 
데이터 
분석 및 
삶의 
영향을 
추론하여 
인물의 
삶에 
대해서 
글쓰기
70
항목
평정점
최상
상
중
하
 제시된 조건을 모두 
포함하였는가?
10
8
6
4
 생애 주기(10대~40대)에 
서술된 주요 사건이 그 
시기에 해당되는가?
10
8
6
4
 서술된 주요 사건의 내용은 
역사적 사실에 부합하는가?
10
8
6
4
 주요 사건과 관련하여 제시 
혹은 분석한 데이터는 
적합한가?
10
8
6
4
 데이터 분석 결과는 
정확한가?
10
8
6
4
 주요 사건이 인물의 삶에 
미친 영향을 추론한 내용은 
인과관계를 담고 있는가?
10
8
6
4
 인물의 삶을 정리한 
내러티브는 사회의 변화를 
보여주고 있는가?
10
8
6
4"""

replacement = """| 평가 요소(배점) | 점수 | 평가 항목 | 최상 | 상 | 중 | 하 |
| --- | --- | --- | --- | --- | --- | --- |
| 인물의 생애주기별 겪었을 주요 사건 관련 데이터 분석 및 삶의 영향을 추론하여 인물의 삶에 대해서 글쓰기 (70) | 70 | 제시된 조건을 모두 포함하였는가? | 10 | 8 | 6 | 4 |
| | | 생애 주기(10대~40대)에 서술된 주요 사건이 그 시기에 해당되는가? | 10 | 8 | 6 | 4 |
| | | 서술된 주요 사건의 내용은 역사적 사실에 부합하는가? | 10 | 8 | 6 | 4 |
| | | 주요 사건과 관련하여 제시 혹은 분석한 데이터는 적합한가? | 10 | 8 | 6 | 4 |
| | | 데이터 분석 결과는 정확한가? | 10 | 8 | 6 | 4 |
| | | 주요 사건이 인물의 삶에 미친 영향을 추론한 내용은 인과관계를 담고 있는가? | 10 | 8 | 6 | 4 |
| | | 인물의 삶을 정리한 내러티브는 사회의 변화를 보여주고 있는가? | 10 | 8 | 6 | 4 |"""

# Using regex to handle potential trailing whitespaces
# We split target into lines and join with \s*
pattern = r'\s*'.join(re.escape(line.strip()) for line in target.strip().split('\n') if line.strip())

# Find and replace
content, count = re.subn(pattern, '\n\n' + replacement + '\n\n', content, count=1)

if count > 0:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Successfully replaced table in ch4_full.md')
else:
    print('Target not found in ch4_full.md')
