import streamlit as st

def run():
    st.markdown('<p class="main-title">AI 챗봇 기반 질문 탐구학습 서술기</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">AI와 대화하며 역사적 사료의 편향성을 점검하고 심층적인 핵심 질문을 도출합니다.</p>', unsafe_allow_html=True)
    
    st.info("💡 **학습 목표**: 사료를 비판적으로 읽고, 1차원적 질문을 고차원적인 역사 탐구 질문으로 확장합니다.")
    
    st.subheader("1. 탐구 사료 선택 및 질문 생성")
    
    with st.container(border=True):
        st.selectbox("탐구할 사료를 선택하세요", ["조선왕조실록 (인조실록)", "단종실록", "기타 사료 직접 입력"])
        
        st.text_area("사료를 읽고 든 1차원적 질문(마중물 질문)을 입력하세요.", placeholder="예) 왜 이 사건이 일어났을까?")
        
        if st.button("AI와 함께 질문 심화하기"):
            if 'gemini_api_key' not in st.session_state:
                st.warning("사이드바에서 API Key를 먼저 입력해주세요.")
            else:
                st.success("AI가 질문을 심화했습니다.")
                st.markdown("""
                **[AI 제안 심화 질문]**
                - 이 사건을 주도한 인물들의 이면적인 의도는 무엇이었을까요?
                - 당시 일반 백성들의 관점에서는 이 사건이 어떻게 기록되었을까요?
                """)
                
    st.divider()
    
    st.subheader("2. 모둠 토의 및 최상 질문 선정")
    st.write("AI가 제안한 질문들을 바탕으로 모둠원과 토의하여 우리 모둠의 '최상 질문'을 선정해보세요.")
    st.text_input("우리 모둠의 최종 핵심 질문")
    
    st.divider()
    
    st.subheader("3. 배.느.궁 (수업 성찰)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_area("배운 점", height=100)
    with col2:
        st.text_area("느낀 점", height=100)
    with col3:
        st.text_area("궁금한 점", height=100)
        
    st.button("결과 제출 및 공유하기", type="primary")
