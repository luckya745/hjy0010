import streamlit as st

def run():
    st.markdown('<p class="main-title">질문 기반 AI 도구 활용 탐구학습 서술기</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">상반된 사료와 데이터를 비교하며 편향성을 극복하고 합리적 역사 판단을 내립니다.</p>', unsafe_allow_html=True)
    
    st.info("💡 **학습 목표**: '같은 사실, 다른 기억'을 주제로 다중 관점의 자료를 분석하고 주체적으로 판단합니다.")
    
    st.subheader("1. 상반된 사료 비교 (의도적 충돌)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔴 관점 A (식민지 수탈론)")
        st.write("일제 강점기 시기 한국의 자원은 일제에 의해 철저히 수탈당했으며, 한국인의 삶은 극도로 피폐해졌다. 토지조사사업과 산미증식계획은 그 대표적인 예이다.")
        # 시각 자료 placeholder
        st.image("https://via.placeholder.com/400x200?text=Data+A", use_container_width=True)
        
    with col2:
        st.markdown("### 🔵 관점 B (식민지 근대화론)")
        st.write("일제 강점기 동안 철도, 항만 등의 인프라가 구축되고 자본주의적 제도가 도입되어 한국 경제 성장의 기반이 마련되었다.")
        # 시각 자료 placeholder
        st.image("https://via.placeholder.com/400x200?text=Data+B", use_container_width=True)
        
    st.divider()
    
    st.subheader("2. AI 팩트체크 및 편향성 검토")
    st.write("위 두 가지 관점에 대해 AI에게 질문하여 숨겨진 맥락이나 편향된 데이터가 없는지 확인해보세요.")
    
    st.text_input("AI에게 물어볼 날카로운 질문 (예: 관점 B에서 언급된 인프라 구축의 실제 수혜자는 누구였는가?)")
    
    if st.button("AI 팩트체크 실행"):
        if 'gemini_api_key' not in st.session_state:
            st.warning("사이드바에서 API Key를 먼저 입력해주세요.")
        else:
            with st.spinner("AI가 두 주장의 근거와 한계를 분석 중입니다..."):
                st.success("팩트체크 완료!")
                st.markdown("""
                **[AI 분석 결과]**
                - 관점 B의 통계는 성장의 결과값을 보여주지만, 그 성장의 열매가 대다수 조선인 농민이 아닌 소수 일본인 지주와 기업가에게 돌아갔다는 분배의 문제를 누락하고 있습니다.
                - 관점 A는 경제적 피해를 강조하지만, 이 시기 형성된 근대적 경험이나 사회 변화의 복합적인 양상을 설명하는 데는 한계가 있을 수 있습니다.
                """)
                
    st.divider()
    st.subheader("3. 최종 판단 및 나의 역사적 서술")
    st.text_area("위의 교차 검증 과정을 거치며 내가 내린 역사적 판단을 서술하세요.", height=150)
    st.button("제출하기", type="primary")
