import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="AI 융합 역사 수업 지원",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 커스텀 CSS 적용 (프리미엄 UI)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.5rem;
    }
    
    .sub-title {
        font-size: 1.2rem;
        font-weight: 400;
        color: #64748B;
        margin-bottom: 2rem;
    }
    
    .st-emotion-cache-16txtl3 {
        padding: 2rem 1.5rem;
    }
    
    .sidebar-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #0F172A;
    }
</style>
""", unsafe_allow_html=True)

# 메인 네비게이션
def main():
    st.sidebar.markdown('<p class="sidebar-title">AI 역사 수업</p>', unsafe_allow_html=True)
    st.sidebar.write("수업 모형을 선택하세요:")
    
    # 4가지 메인 탭 메뉴 구성
    menu = [
        "1. 데이터 과학 활용 사료 탐구 분석기",
        "2. 인물 기반 내러티브 서술기",
        "3. AI 챗봇 기반 질문 탐구학습 서술기",
        "4. 질문 기반 AI 도구 활용 탐구학습 서술기"
    ]
    
    choice = st.sidebar.radio("모드 선택", menu)
    
    st.sidebar.divider()
    
    st.sidebar.markdown("### ⚙️ 설정")
    api_key = st.sidebar.text_input("Gemini API Key 입력", type="password", placeholder="AI 기능 사용을 위해 입력")
    if api_key:
        st.session_state['gemini_api_key'] = api_key
        st.sidebar.success("API Key 적용 완료!")
        
    st.sidebar.info("이 앱은 역사 교과 AI 융합 수업 모형을 기반으로 설계되었습니다.")
    
    # 선택된 메뉴에 따라 해당 모듈 동적 로드 및 실행
    if choice == menu[0]:
        from tabs import tab1_data_analysis
        tab1_data_analysis.run()
    elif choice == menu[1]:
        from tabs import tab2_persona_narrative
        tab2_persona_narrative.run()
    elif choice == menu[2]:
        from tabs import tab3_ai_chatbot
        tab3_ai_chatbot.run()
    elif choice == menu[3]:
        from tabs import tab4_question_inquiry
        tab4_question_inquiry.run()

if __name__ == "__main__":
    main()
