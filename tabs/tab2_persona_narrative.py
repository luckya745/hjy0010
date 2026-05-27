import streamlit as st

def run():
    st.markdown('<p class="main-title">인물 기반 내러티브 서술기</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">가상 인물의 생애 주기와 역사적 사건을 교차하여 1인칭 내러티브를 작성합니다.</p>', unsafe_allow_html=True)
    
    st.info("💡 **학습 목표**: 거시적인 역사적 사건이 개인의 미시적 삶에 미친 영향을 추론하고 공감 능력을 기릅니다.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("👤 페르소나 설정")
        with st.container(border=True):
            st.text_input("가상 인물 이름", "이영숙")
            st.number_input("출생 연도", min_value=1900, max_value=2024, value=1960)
            st.text_area("시대적 배경 및 환경", "서울의 한 노동자 가정에서 태어나 고도 경제 성장과 정치적 민주화를 동시에 겪음.")
            
    with col2:
        st.subheader("📝 생애 주기별 내러티브 작성")
        tab1, tab2, tab3 = st.tabs(["10대", "20대", "30대"])
        
        with tab1:
            st.write("**주요 사건:** 1970년대 대한민국 수출액 및 산업구조 변화")
            st.text_area("당시 데이터가 인물의 삶에 미친 영향", placeholder="데이터를 바탕으로 추론한 내용을 적어보세요...", height=150)
            
        with tab2:
            st.write("**주요 사건:** 1980년대 후반 도시 가구 소득 증가 및 가전제품 보급")
            st.text_area("당시 데이터가 인물의 삶에 미친 영향 ", placeholder="데이터를 바탕으로 추론한 내용을 적어보세요...", height=150)
            
        with tab3:
            st.write("**주요 사건:** 1997년 외환위기 당시 실업률 및 환율 변동")
            st.text_area("당시 데이터가 인물의 삶에 미친 영향  ", placeholder="데이터를 바탕으로 추론한 내용을 적어보세요...", height=150)
            
    st.divider()
    st.subheader("🖋️ 최종 내러티브 완성")
    st.text_area("인물의 관점(1인칭)에서 현대사가 내 삶에 끼친 영향을 종합하여 서술하세요.", height=250)
    
    if st.button("AI 피드백 받기", type="primary"):
        if 'gemini_api_key' not in st.session_state:
            st.warning("사이드바에서 API Key를 먼저 입력해주세요.")
        else:
            with st.spinner("AI가 내러티브의 역사적 정합성을 분석 중입니다..."):
                # AI API 호출 연동 예정
                st.success("피드백이 도착했습니다!")
                st.write("**[AI 역사 교사 피드백]**")
                st.write("해당 시대의 통계 지표와 인물의 체감 감정이 잘 연결되었습니다. 다만 1997년 외환위기 당시의 시대적 맥락이 약간 부족합니다. 이 부분을 보완해보면 어떨까요?")
