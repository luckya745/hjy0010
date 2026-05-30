import streamlit as st

def run():
    st.markdown('<p class="main-title">질문 기반 AI 도구 활용 탐구학습 서술기</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">상반된 사료와 데이터를 비교하며 편향성을 극복하고 합리적 역사 판단을 내립니다.</p>', unsafe_allow_html=True)
    
    st.info("💡 **학습 목표**: '같은 사실, 다른 기억'을 주제로 다중 관점의 자료를 분석하고 주체적으로 판단합니다.")
    
    # 1. 모드 선택
    mode = st.radio("탐구 주제 선택", ["기본 예시 사용 (식민지 수탈론 vs 근대화론)", "직접 입력하기"])
    
    if mode == "기본 예시 사용 (식민지 수탈론 vs 근대화론)":
        event_name = "일제 강점기 식민지 지배의 성격"
        view_a_title = "식민지 수탈론"
        view_a_desc = "일제 강점기 시기 한국의 자원은 일제에 의해 철저히 수탈당했으며, 한국인의 삶은 극도로 피폐해졌다. 토지조사사업과 산미증식계획은 그 대표적인 예이다."
        view_b_title = "식민지 근대화론"
        view_b_desc = "일제 강점기 동안 철도, 항만 등의 인프라가 구축되고 자본주의적 제도가 도입되어 한국 경제 성장의 기반이 마련되었다."
    else:
        st.write("새로운 탐구 주제와 관점을 입력해주세요.")
        event_name = st.text_input("탐구할 역사적 사건 (예: 십자군 전쟁)", "십자군 전쟁")
        
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            view_a_title = st.text_input("관점 A 이름 (예: 종교적 성전)", "종교적 성전")
            view_a_desc = st.text_area("관점 A 내용", "기독교 성지를 탈환하기 위한 성스러운 전쟁이었으며, 신앙심에서 비롯된 정의로운 행동이었다.")
        with col_in2:
            view_b_title = st.text_input("관점 B 이름 (예: 침략과 약탈)", "침략과 약탈")
            view_b_desc = st.text_area("관점 B 내용", "종교를 명분으로 삼았으나 실제로는 영토 확장과 경제적 이익을 노린 잔혹한 침략이자 약탈 전쟁이었다.")
            
    st.divider()
    
    # 6단계 모형 적용
    st.subheader(f"탐구 주제: {event_name}")
    
    # 1단계
    with st.expander("1단계: 질문의 마중물 (사전 지식 확인)", expanded=True):
        st.write(f"**{event_name}**에 대해 평소 어떻게 알고 있었나요? 여러분의 사전 지식이나 느낌을 자유롭게 적어보세요.")
        st.text_area("나의 사전 지식 작성란", key="step1_input")
        
    # 2단계
    with st.expander("2단계: 사고의 반전 (상반된 사료 비교)", expanded=True):
        st.write("하나의 사건에 대해 아래와 같이 다각도의 해석과 인과관계가 존재합니다. 두 관점을 비교해 보세요.")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"### 🔴 관점 A: {view_a_title}")
            st.info(view_a_desc)
        with col2:
            st.markdown(f"### 🔵 관점 B: {view_b_title}")
            st.success(view_b_desc)
            
    # 3단계
    with st.expander("3단계: 관점의 조율 (AI 팩트체크 및 편향성 검토)", expanded=True):
        st.write("두 관점의 타당성과 숨겨진 의도, 편향된 데이터가 없는지 AI에게 날카로운 질문을 던져 팩트체크를 해봅시다.")
        ai_question = st.text_input("AI에게 물어볼 질문 작성 (예: 두 관점에서 누락된 역사적 사실은 무엇인가요?)", key="step3_input")
        
        if st.button("AI 팩트체크 실행", key="btn_factcheck"):
            if 'gemini_api_key' not in st.session_state:
                st.warning("사이드바에서 API Key를 먼저 입력해주세요.")
            else:
                with st.spinner("AI가 두 주장의 근거와 한계를 분석 중입니다..."):
                    st.success("팩트체크 완료!")
                    # 예시 응답 (실제 연동시 AI 생성)
                    st.markdown(f"""
                    **[AI 분석 결과 예시]**
                    - 관점 A({view_a_title})는 특정한 측면을 강조하여 설명하지만, 다른 복합적인 사회 변화를 누락했을 수 있습니다.
                    - 관점 B({view_b_title})는 성과나 결과를 보여주지만, 그 이면에 있는 문제점이나 의도적 측면을 간과하고 있습니다.
                    """)
                    
    # 4단계
    with st.expander("4단계: 비판적 문해 (맥락에 맞는 핵심 선별)", expanded=True):
        st.write("위 AI의 답변을 비판적으로 읽고, 가장 중요하다고 생각되는 핵심 근거나 맥락을 한두 줄로 요약해 보세요.")
        st.text_input("핵심 맥락 선별 및 요약", key="step4_input")
        
    # 5단계
    with st.expander("5단계: 활동 너머의 학습 (역사적 사고력 증진 질문 생성)", expanded=True):
        st.write("지금까지의 탐구 과정을 통해 이 사건에 대해 새롭게 생긴 의문점이나 심화 질문을 하나 만들어 보세요.")
        st.text_input("새로운 꼬리 질문 생성", key="step5_input")
        
    # 6단계
    with st.expander("6단계: 최선의 답 탐색 (나의 최종 역사적 서술)", expanded=True):
        st.write("위의 1~5단계를 모두 종합하여, 인간의 존엄성과 가치에 부합하는 합리적인 판단을 내려봅시다. 나만의 역사적 서술을 완성해 보세요.")
        st.text_area("최종 판단 및 역사적 서술 작성", height=150, key="step6_input")
        if st.button("최종 답안 제출하기", type="primary"):
            st.balloons()
            st.success("훌륭합니다! 탐구학습 서술이 성공적으로 제출되었습니다.")
