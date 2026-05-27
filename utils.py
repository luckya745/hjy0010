import pandas as pd
import numpy as np
import re

def clean_text(text):
    """기본적인 텍스트 정제 함수"""
    if pd.isna(text):
        return ""
    text = re.sub(r'[^\w\s]', '', str(text))
    return text.strip()

# 향후 hanja 라이브러리를 활용한 한자 번역 로직 추가 예정
def translate_hanja(text):
    try:
        import hanja
        return hanja.translate(text, 'substitution')
    except ImportError:
        return text
