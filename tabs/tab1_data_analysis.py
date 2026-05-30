import streamlit as st
import pandas as pd
from visualizer import create_wordcloud, create_network_graph

def run():
    st.markdown('<p class="main-title">데이터 과학 활용 사료 탐구 분석기</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">XML 및 CSV 데이터를 활용하여 역사적 사실을 시각화하고 분석합니다.</p>', unsafe_allow_html=True)
    
    st.info("💡 **학습 목표**: 방대한 역사 데이터를 분석하여 편향성을 줄이고 인과 관계를 구조적으로 파악합니다.")
    
    st.divider()
    
    # 1단계: 자료 수집 및 탐색 단계
    with st.expander("1단계: 자료 수집 및 탐색 단계", expanded=True):
        st.write("공공 데이터 포털 사이트(예: 국사편찬위원회 등)에서 삼국유사, 삼국사기 등의 역사 자료를 검색하고 다운로드하여 업로드하세요.")
        uploaded_file = st.file_uploader("사료 데이터 파일(CSV, XML, TXT, Excel, PDF, PPT) 업로드", type=['csv', 'xml', 'txt', 'xlsx', 'xls', 'pdf', 'pptx', 'ppt'])
        
        if uploaded_file is not None:
            st.success("파일이 성공적으로 업로드되었습니다.")
            if uploaded_file.name.endswith(".xml"):
                st.info("XML 사료 파일 파싱 중... (예: 국사편찬위원회 삼국사기 포맷)")
            elif uploaded_file.name.endswith(".csv"):
                st.info("CSV 데이터 로드 중...")
                
    # 파일이 업로드된 경우에만 2단계 이후 활성화
    show_results = uploaded_file is not None
    
    # 2단계: 자료 가공 및 추론 결과물 발표 단계
    with st.expander("2단계: 자료 가공 및 추론 결과물 발표 단계", expanded=show_results):
        if not show_results:
            st.warning("1단계에서 데이터 파일을 먼저 업로드해주세요.")
        else:
            st.subheader("데이터 시각화 결과")
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
                
            st.write("위 시각화 결과를 바탕으로 발견한 역사적 사실이나 추론 내용을 작성해 보세요.")
            st.text_area("나의 추론 결과 작성", key="tab1_step2_inference")
            
            st.markdown("---")
            st.write("생성형 인공지능(AI)에게 시각화 결과 분석을 요청해 봅시다.")
            ai_prompt = st.text_input("AI 채팅창 프롬프트 작성 (예: 김유신과 가장 밀접하게 연결된 인물은 누구이며 어떤 역사적 의미가 있나요?)", key="tab1_step2_prompt")
            
            if st.button("AI에게 분석 요청", key="btn_tab1_ai"):
                if 'gemini_api_key' not in st.session_state:
                    st.warning("사이드바에서 API Key를 먼저 입력해주세요.")
                else:
                    with st.spinner("AI가 데이터를 분석 중입니다..."):
                        st.success("AI 분석 완료!")
                        st.markdown("""
                        **[AI 분석 결과 예시]**
                        시각화된 네트워크 관계도에 따르면 '김유신'과 '김춘추'의 연결 강도가 가장 높게 나타납니다. 이는 삼국통일 과정에서 두 인물이 정치적, 군사적으로 매우 밀접하게 협력했음을 데이터가 보여주고 있습니다. 반면 '의자왕'과 '계백'은 별도의 군집을 이루고 있어, 신라와 백제 진영이 명확히 대비됨을 시각적으로 확인할 수 있습니다.
                        """)
                        
    # 3단계: 활동 결과를 바탕으로 학습주제 학습 단계
    with st.expander("3단계: 활동 결과를 바탕으로 학습주제 학습 단계 (결과물 검증)", expanded=show_results):
        if not show_results:
            st.warning("1단계에서 데이터 파일을 먼저 업로드해주세요.")
        else:
            st.write("2단계에서 도출한 나의 추론이나 AI의 분석 결과를 기존의 역사적 사실(교과서, 사료 등)과 비교하여 타당성을 검증해 봅시다.")
            st.text_area("검증 결과 작성 (오류나 편향성 검토)", key="tab1_step3_validation")
            
    # 4단계: 학습을 바탕으로 결과물 수정 단계
    with st.expander("4단계: 학습을 바탕으로 결과물 수정 단계", expanded=show_results):
        if not show_results:
            st.warning("1단계에서 데이터 파일을 먼저 업로드해주세요.")
        else:
            st.write("3단계의 검증 과정과 피드백을 바탕으로, 처음에 작성했던 추론 결과물을 수정·보완하여 최종 역사적 서술을 완성해 보세요.")
            st.text_area("최종 결과물(역사적 서술) 작성", height=150, key="tab1_step4_final")
            if st.button("최종 답안 제출하기", type="primary", key="btn_tab1_submit"):
                st.balloons()
                st.success("데이터 과학을 활용한 사료 탐구가 훌륭하게 완료되었습니다!")
