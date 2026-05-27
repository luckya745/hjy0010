import streamlit as st
import pandas as pd
from visualizer import create_wordcloud, create_network_graph

def run():
    st.markdown('<p class="main-title">데이터 과학 활용 사료 탐구 분석기</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">XML 및 CSV 데이터를 활용하여 역사적 사실을 시각화하고 분석합니다.</p>', unsafe_allow_html=True)
    
    st.info("💡 **학습 목표**: 방대한 역사 데이터를 분석하여 편향성을 줄이고 인과 관계를 구조적으로 파악합니다.")
    
    # 임시 UI 구성
    st.subheader("1. 데이터 파일 업로드")
    uploaded_file = st.file_uploader("사료 데이터 파일(CSV, XML, TXT) 업로드", type=['csv', 'xml', 'txt'])
    
    if uploaded_file is not None:
        st.success("파일이 성공적으로 업로드되었습니다.")
        
        # 파일 형식에 따른 파싱 안내
        if uploaded_file.name.endswith(".xml"):
            st.info("XML 사료 파일 파싱 중... (예: 국사편찬위원회 삼국사기 포맷)")
        elif uploaded_file.name.endswith(".csv"):
            st.info("CSV 데이터 로드 중...")
            
        st.divider()
        st.subheader("2. 데이터 시각화 결과")
        col1, col2 = st.columns(2)
        
        # 시뮬레이션용 데이터
        sample_word_freq = {"김유신": 85, "김춘추": 70, "선덕여왕": 65, "의자왕": 40, "계백": 35}
        sample_adj_matrix = pd.DataFrame(
            [[0, 5, 3, 0, 0], [5, 0, 4, 1, 0], [3, 4, 0, 0, 0], [0, 1, 0, 0, 6], [0, 0, 0, 6, 0]],
            columns=["김유신", "김춘추", "선덕여왕", "의자왕", "계백"],
            index=["김유신", "김춘추", "선덕여왕", "의자왕", "계백"]
        )
        
        with col1:
            st.write("**[워드 클라우드]**")
            st.caption("주요 키워드의 빈도를 시각화합니다.")
            fig_wc = create_wordcloud(sample_word_freq)
            st.pyplot(fig_wc)
            
        with col2:
            st.write("**[네트워크 관계도]**")
            st.caption("인물 또는 사건 간의 동시 출현 관계를 분석합니다.")
            fig_net = create_network_graph(sample_adj_matrix)
            st.pyplot(fig_net)
