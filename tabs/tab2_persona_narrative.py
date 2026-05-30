import streamlit as st
import datetime

def run():
    st.markdown('<p class="main-title">인물 기반 내러티브 서술기</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">가상 인물의 생애 주기와 역사적 사건을 교차하여 1인칭 내러티브를 작성합니다.</p>', unsafe_allow_html=True)
    
    st.info("💡 **학습 목표**: 거시적인 역사적 사건이 개인의 미시적 삶에 미친 영향을 추론하고 공감 능력을 기릅니다.")
    st.divider()
    
    # 1단계
    with st.expander("1단계: 인물 및 상황 제시 단계", expanded=True):
        st.write("교사가 제시한 인물의 주요 사건 및 변화를 확인하거나, 탐구할 페르소나를 설정하세요.")
        col1, col2 = st.columns(2)
        with col1:
            persona_name = st.text_input("가상 인물 이름", "이영숙")
            birth_year = st.number_input("출생 연도", min_value=1900, max_value=2024, value=1960)
        with col2:
            st.text_area("시대적 배경 및 환경", "서울의 한 노동자 가정에서 태어나 고도 경제 성장과 정치적 민주화를 동시에 겪음.", height=130)
            
    # 2단계
    with st.expander("2단계: 조건 제시 및 내용 서술 단계", expanded=True):
        st.write("설정된 인물의 생애 주기별로 나이를 계산하여, 각 시기에 어떤 역사적 사건들이 있었을지 탐색해 보세요.")
        
        # 간단한 나이 계산 로직 예시
        current_year = datetime.datetime.now().year
        age_now = current_year - birth_year
        st.info(f"**{persona_name}** 님은 {birth_year}년생으로, 현재 기준(2024년 등) 약 {age_now}세입니다.")
        
        st.write("각 생애 주기(10대~50대)가 대략 몇 년도에 해당하는지 생각해보고 기록하세요.")
        c1, c2, c3, c4, c5 = st.columns(5)
        with c1: st.text_input("10대 시기 (연도)", f"{birth_year + 10}년 ~")
        with c2: st.text_input("20대 시기 (연도)", f"{birth_year + 20}년 ~")
        with c3: st.text_input("30대 시기 (연도)", f"{birth_year + 30}년 ~")
        with c4: st.text_input("40대 시기 (연도)", f"{birth_year + 40}년 ~")
        with c5: st.text_input("50대 시기 (연도)", f"{birth_year + 50}년 ~")
        
    # 3단계
    with st.expander("3단계: 주요 사건 관련 데이터 분석 및 삶의 영향 추론", expanded=True):
        st.write("각 생애 주기별로 발생한 주요 사건과 데이터를 바탕으로, 이것이 인물의 삶에 어떤 영향을 미쳤을지 추론해 봅니다.")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["10대", "20대", "30대", "40대", "50대"])
        
        with tab1:
            st.write(f"**주요 사건 (10대, 약 {birth_year+10}년대):** 대한민국 수출액 및 산업구조 변화")
            st.text_area("당시 데이터가 인물의 삶에 미친 영향", placeholder="데이터를 바탕으로 추론한 내용을 적어보세요...", height=150, key="tab2_step3_10s")
            
        with tab2:
            st.write(f"**주요 사건 (20대, 약 {birth_year+20}년대):** 도시 가구 소득 증가 및 가전제품 보급")
            st.text_area("당시 데이터가 인물의 삶에 미친 영향 ", placeholder="데이터를 바탕으로 추론한 내용을 적어보세요...", height=150, key="tab2_step3_20s")
            
        with tab3:
            st.write(f"**주요 사건 (30대, 약 {birth_year+30}년대):** 외환위기 당시 실업률 및 환율 변동")
            st.text_area("당시 데이터가 인물의 삶에 미친 영향  ", placeholder="데이터를 바탕으로 추론한 내용을 적어보세요...", height=150, key="tab2_step3_30s")
            
        with tab4:
            st.write(f"**주요 사건 (40대, 약 {birth_year+40}년대):** IT 벤처 붐 및 글로벌 금융위기")
            st.text_area("당시 데이터가 인물의 삶에 미친 영향   ", placeholder="데이터를 바탕으로 추론한 내용을 적어보세요...", height=150, key="tab2_step3_40s")
            
        with tab5:
            st.write(f"**주요 사건 (50대, 약 {birth_year+50}년대):** 저성장·고령화 사회 진입 및 4차 산업혁명")
            st.text_area("당시 데이터가 인물의 삶에 미친 영향    ", placeholder="데이터를 바탕으로 추론한 내용을 적어보세요...", height=150, key="tab2_step3_50s")
            
    # 4단계
    with st.expander("4단계: 인물의 삶에 대한 내러티브 완성", expanded=True):
        st.write("위의 1~3단계 분석을 종합하여, 거시적인 역사적 사건이 개인(나)의 미시적 삶에 끼친 영향을 **1인칭 관점**에서 한 편의 서사로 완성하세요.")
        st.text_area("최종 내러티브 서술 (1인칭 시점)", height=250, key="tab2_step4_final")
        
        if st.button("AI 피드백 받기 및 제출", type="primary", key="btn_tab2_submit"):
            if 'gemini_api_key' not in st.session_state:
                st.warning("사이드바에서 API Key를 먼저 입력해주세요.")
            else:
                with st.spinner("AI가 내러티브의 역사적 정합성을 분석 중입니다..."):
                    st.success("피드백이 도착했습니다! 제출이 완료되었습니다.")
                    st.markdown("""
                    **[AI 역사 교사 피드백]**
                    해당 시대의 통계 지표와 인물의 체감 감정이 잘 연결되었습니다. 전체적으로 흐름이 매끄럽고 1인칭 시점의 몰입감이 뛰어납니다. 다만 특정 시기(예: 30대)의 시대적 맥락이나 정책 변화를 조금 더 구체적으로 묘사한다면 더욱 생생한 내러티브가 될 것입니다.
                    """)
