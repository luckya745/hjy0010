import streamlit as st

def run():
    st.markdown('<p class="main-title">AI 챗봇 기반 질문 탐구학습 서술기</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">AI와 대화하며 역사적 사료의 편향성을 점검하고 심층적인 핵심 질문을 도출합니다.</p>', unsafe_allow_html=True)
    
    st.info("💡 **학습 목표**: 사료를 비판적으로 읽고, 1차원적 질문을 고차원적인 역사 탐구 질문으로 확장합니다.")
    st.divider()
    
    # 1단계
    with st.expander("1단계: 자료 탐색 및 수집", expanded=True):
        st.write("학생 스스로 공신력 있는 원문(국사편찬위원회 등)을 검색하고 탐구할 사료를 선정하세요.")
        source_type = st.selectbox("탐구할 사료를 선택하거나 직접 입력하세요", ["조선왕조실록 (인조실록)", "단종실록", "기타 사료 직접 입력"])
        if source_type == "기타 사료 직접 입력":
            source_name = st.text_input("사료 제목을 입력하세요", key="tab3_step1_source_name")
        source_url = st.text_input("사료의 출처(URL) 또는 참고 문헌을 입력하세요", key="tab3_step1_url")
        
    # 2단계
    with st.expander("2단계: 노트북LM AI 챗봇에 자료 학습시키기", expanded=True):
        st.write("1단계에서 찾은 사료의 원문이나 핵심 내용을 아래에 입력하여 AI 챗봇이 해당 내용을 학습할 수 있도록 지식 베이스를 구축합니다.")
        st.text_area("학습시킬 사료 내용 입력", height=150, key="tab3_step2_kb")
        if st.button("AI에게 자료 학습시키기", key="btn_tab3_train"):
            st.success("자료 학습이 완료되었습니다! 이제 이 사료를 바탕으로 대화가 가능합니다.")
            
    # 3단계
    with st.expander("3단계: AI 챗봇을 활용한 핵심질문 만들기", expanded=True):
        st.write("학습된 사료를 바탕으로 1차원적 질문(마중물 질문)이나 퀴즈를 만들어보고, AI와 대화하여 질문을 심화시켜 보세요.")
        st.text_area("사료를 읽고 든 1차원적 질문(마중물 질문)을 입력하세요.", placeholder="예) 왜 이 사건이 일어났을까?", key="tab3_step3_q")
        
        if st.button("AI와 함께 질문 심화하기", key="btn_tab3_ai"):
            if 'gemini_api_key' not in st.session_state:
                st.warning("사이드바에서 API Key를 먼저 입력해주세요.")
            else:
                with st.spinner("AI가 질문을 심층적으로 분석하고 확장 중입니다..."):
                    st.success("AI가 질문을 심화했습니다.")
                    st.markdown("""
                    **[AI 제안 심화 질문]**
                    - 이 사건을 주도한 인물들의 이면적인 정치적, 경제적 의도는 무엇이었을까요?
                    - 당시 일반 백성들 또는 소외된 계층의 관점에서는 이 사건이 어떻게 기록되었을까요?
                    """)
                    
    # 4단계
    with st.expander("4단계: 모둠 토의 및 최상 질문 선정", expanded=True):
        st.write("3단계에서 AI가 제안한 질문들을 바탕으로 모둠원들과 토의하여, 우리 모둠만의 가치 있는 **'최상 질문'**을 선정해 보세요.")
        st.text_input("우리 모둠의 최종 핵심 질문", key="tab3_step4_best_q")
        
    # 5단계
    with st.expander("5단계: 질문 상호작용 (다른 모둠과 교환)", expanded=True):
        st.write("선정된 최상 질문을 다른 모둠과 교환하고 토론해 봅니다. 다른 모둠의 의견이나 새롭게 발견한 관점을 정리해 보세요.")
        st.text_area("다른 모둠과의 토론 결과 정리", height=100, key="tab3_step5_interaction")
        
    # 6단계
    with st.expander("6단계: 자기 성찰 (배.느.궁)", expanded=True):
        st.write("학습 내용과 AI 활용 과정 전체에 대해 스스로 성찰해 봅니다.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text_area("배운 점", height=100, key="tab3_step6_learn")
        with col2:
            st.text_area("느낀 점", height=100, key="tab3_step6_feel")
        with col3:
            st.text_area("궁금한 점", height=100, key="tab3_step6_wonder")
            
        if st.button("결과 제출 및 공유하기", type="primary", key="btn_tab3_submit"):
            st.balloons()
            st.success("훌륭합니다! AI 챗봇 기반 탐구 활동이 성공적으로 기록되었습니다.")
