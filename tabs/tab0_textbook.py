import streamlit as st
import os
import re
from cryptography.fernet import Fernet

def run():
    st.markdown('<div class="main-title">연수교재 본문 확인하기</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">PDF 교재 본문을 영구박제하여 확인합니다.</div>', unsafe_allow_html=True)
    
    base_path = os.path.dirname(__file__)
    
    # Secrets에서 암호화 키 가져오기
    enc_key = st.secrets.get("ENCRYPTION_KEY", None)
    fernet = Fernet(enc_key) if enc_key else None
    
    # 공통 보기 옵션
    if "global_view_mode" not in st.session_state:
        st.session_state.global_view_mode = "요약본"
        
    view_mode = st.radio("전체 교재 보기 옵션", ["요약본", "전체본"], horizontal=True, 
                         index=0 if st.session_state.global_view_mode == "요약본" else 1)
    
    if view_mode != st.session_state.global_view_mode:
        st.session_state.global_view_mode = view_mode
        # 모드가 바뀌면 첫 페이지로 리셋
        st.session_state.global_page_idx = 0
        st.session_state.search_matches = []
        st.session_state.current_match_idx = -1
        st.rerun()

    # 데이터 로드
    all_pages = []
    chapter_start_indices = [] # 각 챕터의 시작 global index 저장
    
    for i in range(6):
        if view_mode == "전체본":
            target_file = f"ch{i+1}_full.md"
        else:
            target_file = f"ch{i+1}.md"
            
        enc_file_path = os.path.join(base_path, f"{target_file}.enc")
        file_path = os.path.join(base_path, target_file)
        
        content = ""
        if os.path.exists(enc_file_path):
            if fernet:
                try:
                    with open(enc_file_path, "rb") as f:
                        encrypted_data = f.read()
                    decrypted_data = fernet.decrypt(encrypted_data)
                    content = decrypted_data.decode("utf-8")
                except Exception as e:
                    st.error(f"데이터 복호화 중 오류가 발생했습니다. (제 {i+1}장) : {e}")
            else:
                st.error("암호화 키(ENCRYPTION_KEY)가 설정되지 않았습니다.")
        elif os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            st.warning(f"제 {i+1}장 ({view_mode}) 데이터를 불러올 수 없습니다.")
            
        if content:
            if view_mode == "전체본":
                pages = re.split(r'\s*---PAGE_BREAK---\s*', content)
            else:
                pages = [content]
            
            chapter_start_indices.append(len(all_pages))
            for local_idx, p in enumerate(pages):
                all_pages.append({
                    "chapter": i + 1,
                    "local_idx": local_idx,
                    "content": p
                })
        else:
            chapter_start_indices.append(len(all_pages))

    total_pages = len(all_pages)
    
    if total_pages == 0:
        st.info("표시할 내용이 없습니다.")
        return

    # 세션 상태 초기화
    if "global_page_idx" not in st.session_state:
        st.session_state.global_page_idx = 0
    if "search_matches" not in st.session_state:
        st.session_state.search_matches = []
    if "current_match_idx" not in st.session_state:
        st.session_state.current_match_idx = -1
        
    current_page = st.session_state.global_page_idx
    if current_page >= total_pages:
        current_page = max(0, total_pages - 1)
        st.session_state.global_page_idx = current_page
        
    current_chapter = all_pages[current_page]["chapter"] if total_pages > 0 else 1

    # 챕터 선택 UI
    st.markdown("**챕터 이동**")
    cols = st.columns(6)
    for i in range(6):
        with cols[i]:
            btn_type = "primary" if current_chapter == i + 1 else "secondary"
            if st.button(f"{i+1}장", key=f"btn_chap_{i}", type=btn_type, use_container_width=True):
                # 이동할 챕터의 페이지가 존재하는지 확인
                if i < len(chapter_start_indices) and chapter_start_indices[i] < total_pages:
                    st.session_state.global_page_idx = chapter_start_indices[i]
                    st.session_state.search_matches = []
                    st.rerun()
                else:
                    st.warning(f"{i+1}장의 내용을 불러올 수 없습니다.")

    # 현재 페이지 내용 출력
    st.markdown("---")
    st.markdown(all_pages[current_page]["content"])
    st.markdown("---")
    
    # 네비게이션
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if current_page > 0:
            if st.button("⬅️ 이전 페이지", use_container_width=True):
                st.session_state.global_page_idx -= 1
                st.rerun()
    with col2:
        st.markdown(f"<div style='text-align: center;'><b>전체 {current_page + 1} / {total_pages} 페이지 (제 {current_chapter}장)</b></div>", unsafe_allow_html=True)
    with col3:
        if current_page < total_pages - 1:
            if st.button("다음 페이지 ➡️", use_container_width=True):
                st.session_state.global_page_idx += 1
                st.rerun()
                
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 검색 영역
    search_col1, search_col2, search_col3 = st.columns([1.5, 2, 1.5])
    
    with search_col1:
        st.markdown("**페이지 이동**")
        sub_col1, sub_col2 = st.columns([3, 1])
        with sub_col1:
            search_page = st.number_input("페이지 번호 입력", min_value=1, max_value=total_pages, value=current_page + 1, step=1, label_visibility="collapsed")
        with sub_col2:
            if st.button("이동", key="go_page", use_container_width=True):
                st.session_state.global_page_idx = search_page - 1
                st.session_state.search_matches = []
                st.rerun()
                
    with search_col2:
        st.markdown("**단어 전체 검색**")
        word_col1, word_col2 = st.columns([3, 1])
        with word_col1:
            search_word = st.text_input("단어 검색", placeholder="검색할 단어 입력", label_visibility="collapsed")
        with word_col2:
            if st.button("검색", key="go_word", use_container_width=True):
                matches = []
                for idx, p in enumerate(all_pages):
                    if search_word and search_word.lower() in p["content"].lower():
                        matches.append(idx)
                
                if matches:
                    st.session_state.search_matches = matches
                    next_idx = -1
                    for i, match_page in enumerate(matches):
                        if match_page >= current_page:
                            next_idx = i
                            break
                    if next_idx == -1:
                        next_idx = 0 
                        
                    st.session_state.current_match_idx = next_idx
                    st.session_state.global_page_idx = matches[next_idx]
                    st.rerun()
                elif search_word:
                    st.warning(f"'{search_word}' 단어를 찾을 수 없습니다.")
                    st.session_state.search_matches = []
                    st.session_state.current_match_idx = -1
                    
        # 검색 결과 네비게이션
        if st.session_state.get("search_matches"):
            matches = st.session_state.search_matches
            m_idx = st.session_state.current_match_idx
            
            nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
            with nav_col1:
                if st.button("⬅️ 이전", key="prev_match", use_container_width=True):
                    new_idx = (m_idx - 1) % len(matches)
                    st.session_state.current_match_idx = new_idx
                    st.session_state.global_page_idx = matches[new_idx]
                    st.rerun()
            with nav_col2:
                st.markdown(f"<div style='text-align: center; font-size: 0.9em; padding-top: 5px;'>검색결과: <b>{m_idx + 1} / {len(matches)}</b></div>", unsafe_allow_html=True)
            with nav_col3:
                if st.button("다음 ➡️", key="next_match", use_container_width=True):
                    new_idx = (m_idx + 1) % len(matches)
                    st.session_state.current_match_idx = new_idx
                    st.session_state.global_page_idx = matches[new_idx]
                    st.rerun()
