import re

filename = r'c:\Users\User\Downloads\history_aiedu_app\tabs\ch6_full.md'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <자료 1~2>, <자료 3~4>, <자료 5~6>, <질문 1~7>, <자료 1~6> 
# to escape the tildes.
content = content.replace('<자료 1~2>', '<자료 1\~2>')
content = content.replace('<자료 3~4>', '<자료 3\~4>')
content = content.replace('<자료 5~6>', '<자료 5\~6>')
content = content.replace('<질문 1~7>', '<질문 1\~7>')
content = content.replace('<자료 1~6>', '<자료 1\~6>')

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated ch6_full.md')
