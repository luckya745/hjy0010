import streamlit as st

def run():
    st.markdown('<div class="main-title">연수교재 본문 확인하기</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">PDF 교재 본문을 영구박제하여 확인합니다.</div>', unsafe_allow_html=True)
    
    import os
    
    # 1장부터 6장까지 탭 구성
    tabs = st.tabs(["1장", "2장", "3장", "4장", "5장", "6장"])
    
    base_path = os.path.dirname(__file__)
    
    from cryptography.fernet import Fernet
    
    # Secrets에서 암호화 키 가져오기
    enc_key = st.secrets.get("ENCRYPTION_KEY", None)
    fernet = Fernet(enc_key) if enc_key else None
    
    def render_content(content_str, is_full_mode, chap_idx, is_local=False):
        pages = content_str.split("\n\n---PAGE_BREAK---\n\n")
        if is_full_mode and len(pages) > 1:
            prefix = "local_" if is_local else ""
            page_key = f"chap_{prefix}{chap_idx}_page"
            if page_key not in st.session_state:
                st.session_state[page_key] = 0
            
            current_page = st.session_state[page_key]
            if current_page >= len(pages):
                current_page = len(pages) - 1
                st.session_state[page_key] = current_page
                
            st.markdown(pages[current_page])
            st.markdown("---")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                if current_page > 0:
                    if st.button("⬅️ 이전 페이지", key=f"prev_{prefix}{chap_idx}"):
                        st.session_state[page_key] -= 1
                        st.rerun()
            with col2:
                st.markdown(f"<div style='text-align: center;'><b>{current_page + 1} / {len(pages)}</b></div>", unsafe_allow_html=True)
            with col3:
                if current_page < len(pages) - 1:
                    if st.button("다음 페이지 ➡️", key=f"next_{prefix}{chap_idx}"):
                        st.session_state[page_key] += 1
                        st.rerun()
        else:
            st.markdown(content_str)
            
    for i in range(6):
        with tabs[i]:
            view_mode = st.radio(f"제 {i+1}장 보기 옵션", ["요약본", "전체본"], horizontal=True, key=f"view_mode_{i}")
            
            if view_mode == "전체본":
                target_file = f"ch{i+1}_full.md"
            else:
                target_file = f"ch{i+1}.md"
                
            enc_file_path = os.path.join(base_path, f"{target_file}.enc")
            file_path = os.path.join(base_path, target_file)
            
            if os.path.exists(enc_file_path):
                if fernet:
                    try:
                        with open(enc_file_path, "rb") as f:
                            encrypted_data = f.read()
                        decrypted_data = fernet.decrypt(encrypted_data)
                        content = decrypted_data.decode("utf-8")
                        render_content(content, view_mode == "전체본", i)
                    except Exception as e:
                        st.error(f"데이터 복호화 중 오류가 발생했습니다. (키를 확인하세요) : {e}")
                else:
                    st.error("암호화 키(ENCRYPTION_KEY)가 설정되지 않았습니다. Streamlit Secrets 설정을 확인하세요.")
            elif os.path.exists(file_path):
                # 원본 파일이 있는 경우 (아직 암호화하지 않은 로컬 환경용)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                render_content(content, view_mode == "전체본", i, is_local=True)
            else:
                st.error(f"제 {i+1}장 ({view_mode}) 데이터를 불러올 수 없습니다.")
