import matplotlib.pyplot as plt
import networkx as nx
from wordcloud import WordCloud
import streamlit as st

def set_korean_font():
    """운영체제에 따른 한글 폰트 설정"""
    import platform
    if platform.system() == 'Windows':
        plt.rcParams['font.family'] = 'Malgun Gothic'
    elif platform.system() == 'Darwin':
        plt.rcParams['font.family'] = 'AppleGothic'
    else:
        plt.rcParams['font.family'] = 'NanumGothic'
    plt.rcParams['axes.unicode_minus'] = False

def create_wordcloud(word_freq):
    """단어 빈도 딕셔너리를 받아 워드클라우드 Figure 반환"""
    set_korean_font()
    font_path = None
    import platform
    if platform.system() == 'Windows':
        font_path = 'C:/Windows/Fonts/malgun.ttf'
    elif platform.system() == 'Darwin':
        font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'
        
    wc = WordCloud(
        font_path=font_path,
        background_color='white',
        width=800,
        height=400
    )
    
    # 딕셔너리가 비어있으면 기본값 처리
    if not word_freq:
        word_freq = {"데이터없음": 1}
        
    cloud = wc.generate_from_frequencies(word_freq)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(cloud, interpolation='bilinear')
    ax.axis('off')
    return fig

def create_network_graph(relationship_df):
    """관계 데이터프레임을 받아 네트워크 그래프 Figure 반환"""
    set_korean_font()
    G = nx.from_pandas_adjacency(relationship_df)
    
    # 고립된 노드 제거
    G.remove_nodes_from(list(nx.isolates(G)))
    
    fig, ax = plt.subplots(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.5)
    
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=2000, 
            node_color="skyblue", font_family=plt.rcParams['font.family'], 
            font_size=10, edge_color="gray", alpha=0.6)
            
    ax.set_title("인물 네트워크 관계도", fontsize=15)
    return fig
