from cgitb import text
import keyword
from multiprocessing.sharedctypes import Value
import streamlit as st
import random

main_count = 0

list_genre = [ "社交ダンス", "ストリートダンス", "ヒップホップ", "ジャズダンス", "ベリーダンス", "ラテンダンス", "バレエダンス", "チアダンス" ]
list_odo = [ "トラフィック・ジャム　踊ってみた / めーとる・りた", "惑星ループ　踊ってみた / 小豆", "だから僕は音楽を辞めた　踊ってみた / ありく×", "クレイジー・ビート　踊ってみた / SLH × アナタシア", "ボトム　踊ってみた / ありく", "DAYBREAK FRONTLINE　踊ってみた / 佐藤家", "チェリーハント　踊ってみた / になぺん×とらゲッツ", "夜行性ハイズ　踊ってみた / ありく", "金曜日のおはよう　踊ってみた / まなこ", "おねがいダーリン　踊ってみた / 仮面ライヤー217", "ラブカ？　踊ってみた / 梅かっぱ×ぽるし" ]
list_dgu = [ "レッスンウェア", "ダンスシューズ", "タオル", "飲み物", "髪留め", "全身鏡", "スピーカー", "汗対策グッズ", "動きやすい服" ]
list_song = [ "「デレステ」Secret Daybreak", "常夜燈 / PEOPLE1", "HEROHERO / Vaundy", "青と夏 / Mrs. GREEN APPLE", "蒼のワルツ / Eve", "Le reve / mossari" ]

ran_genre = random.choice(list_genre)
ran_odo = random.choice(list_odo) 
ran_dgu = random.choice(list_dgu) 
ran_song = random.choice(list_song)


link = '[ポーズの画像認識](https://teachablemachine.withgoogle.com/models/CYSA2hsCY/)'
st.sidebar.markdown(link, unsafe_allow_html = True)
    
link = '[アイドルの画像認識](https://teachablemachine.withgoogle.com/models/aXKUL8nS7/)'
st.sidebar.markdown(link, unsafe_allow_html = True)

st.title("人工知能基礎　チャットボット")
    
st.write("---")
st.write("""
    
    ##### ダンスのジャンル
    ##### おすすめの踊ってみた動画
    ##### ダンスに必要な道具
    ##### 踊ってほしい曲を言ってくれるよ！
        
""")
    
st.write("---")


def main():
    
    text = st.text_input(label='ここに入力して', value = '')
    if st.button("送信"):
        
        if "ジャンル" in text:
            st.write("わたし ＞", text)
            st.write("あいちゃん＞", ran_genre, "を踊ってみてはどうですの〜！")
            
        if "動画" in text:
            st.write("わたし ＞", text)
            st.write("あいちゃん ＞", ran_odo, "を見てみてくださる〜？")
            
        if "道具" in text:
            st.write("わたし ＞", text)
            st.write("あいちゃん ＞", "必要な道具は", ran_dgu, "ですわ〜！")
        
        if "曲" in text:
            st.write("わたし ＞", text)
            st.write("あいちゃん ＞", "おすすめは", ran_song, "ですわ〜！")
        
    st.write("---")

main()