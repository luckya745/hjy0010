import fitz
import os
import re

pdf_path = r'C:\Users\User\.gemini\antigravity\교과 융합 한글 파일 양식 (역사) 합본.pdf'
doc = fitz.open(pdf_path)
bounds = [0, 39, 74, 112, 154, 188, doc.page_count]
tabs_path = r'c:\Users\User\Downloads\history_aiedu_app\tabs'

i = 3 # Chapter 4
start = bounds[i]
end = bounds[i+1]
text = []
for page_num in range(start, end):
    page = doc[page_num]
    page_text = page.get_text()
    
    # Format page number
    lines = page_text.strip().split('\n')
    if lines and lines[0].isdigit():
        lines[0] = f"{lines[0]}page\n"
    page_text = '\n'.join(lines)
    
    # Fix CHAPTER
    page_text = re.sub(r'CHAPTER\s*\n(.*?)\s*\n(0[1-6])', r'# CHAPTER \2 \1\n', page_text)
    
    # Fix Subheadings
    page_text = re.sub(r'^(0[1-9]\.\s.*)', r'## \1\n', page_text, flags=re.MULTILINE)
    
    text.append(page_text)

final_text = "\n\n---PAGE_BREAK---\n\n".join(text)

out_path = os.path.join(tabs_path, f'ch{i+1}_full.md')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(final_text)
print(f"Created ch{i+1}_full.md ({len(final_text)} bytes)")
