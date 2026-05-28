import streamlit as st

def run():
    st.markdown('<div class="main-title">연수교재 본문 확인하기</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">PDF 교재 본문을 영구박제하여 확인합니다.</div>', unsafe_allow_html=True)
    
    import os
    
    # 1장부터 6장까지 탭 구성
    tabs = st.tabs(["1장", "2장", "3장", "4장", "5장", "6장"])
    
    base_path = os.path.dirname(__file__)
    
    for i in range(6):
        file_path = os.path.join(base_path, f"ch{i+1}.md")
        with tabs[i]:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                st.markdown(content)
            else:
                st.error(f"제 {i+1}장 데이터를 불러올 수 없습니다.")
