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
    
    for i in range(6):
        enc_file_path = os.path.join(base_path, f"ch{i+1}.md.enc")
        file_path = os.path.join(base_path, f"ch{i+1}.md") # 로컬 원본 파일 (개발용 폴백)
        
        with tabs[i]:
            if os.path.exists(enc_file_path):
                if fernet:
                    try:
                        with open(enc_file_path, "rb") as f:
                            encrypted_data = f.read()
                        decrypted_data = fernet.decrypt(encrypted_data)
                        content = decrypted_data.decode("utf-8")
                        st.markdown(content)
                    except Exception as e:
                        st.error(f"데이터 복호화 중 오류가 발생했습니다. (키를 확인하세요) : {e}")
                else:
                    st.error("암호화 키(ENCRYPTION_KEY)가 설정되지 않았습니다. Streamlit Secrets 설정을 확인하세요.")
            elif os.path.exists(file_path):
                # 원본 파일이 있는 경우 (아직 암호화하지 않은 로컬 환경용)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                st.markdown(content)
            else:
                st.error(f"제 {i+1}장 데이터를 불러올 수 없습니다.")
