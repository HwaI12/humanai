import streamlit as st
import numpy as np
import time

st.set_page_config(layout="wide")
#セレクトボックスのリストを作成
pagelist = ["page1","page2"]
#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択",pagelist)
if selector=="page1":
    y = 0
    A = 1
    fre = [0] + [440.0 * 2.0**((i-9)/12.0) for i in range(24)]
    rate = 48000
    BPM = 106
    note_len = [4, 4, 4, 4, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 4, 4, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 4, 4, 2]
    codes = ['R', 'R', 'Asu', 'Aa', 'D', 'ACs', 'Bm', 'Asu', 'Aa', 'G', 'DFs', 'Bm', 'G', 'Aa', 'Asu', 'Aa', 'D', 'ACs', 'Bm', 'Asu', 'Aa', 'G', 'DFs', 'Bm', 'G', 'Aa', 'D', 'R', 'R']

    for r,n in zip(note_len,codes):
        t = (120/BPM) * 2/r
        n_len = np.arange(0, t, 1/rate)
        if n=='R':
            code = A*np.sin(2*np.pi*fre[0]*n_len) + A*np.sin(2*np.pi*fre[0]*n_len) + A*np.sin(2*np.pi*fre[0]*n_len)
            y = np.append(y, code)
        elif n=='Asu':
            code = A*np.sin(2*np.pi*fre[10]*n_len) + A*np.sin(2*np.pi*fre[15]*n_len) + A*np.sin(2*np.pi*fre[17]*n_len) #ラレミ
            y = np.append(y, code)
        elif n=='Aa':
            code = A*np.sin(2*np.pi*fre[10]*n_len) + A*np.sin(2*np.pi*fre[14]*n_len) + A*np.sin(2*np.pi*fre[17]*n_len)#ラド#ミ
            y = np.append(y, code)
        elif n=='D':
            code = A*np.sin(2*np.pi*fre[3]*n_len) + A*np.sin(2*np.pi*fre[7]*n_len) + A*np.sin(2*np.pi*fre[10]*n_len) #レファ#ラ
            y = np.append(y, code)
        elif n=='ACs':
            code = A*np.sin(2*np.pi*fre[14]*n_len) + A*np.sin(2*np.pi*fre[17]*n_len) + A*np.sin(2*np.pi*fre[22]*n_len) #ド#ミラ
            y = np.append(y, code)
        elif n=='Bm':
            code = A*np.sin(2*np.pi*fre[12]*n_len) + A*np.sin(2*np.pi*fre[15]*n_len) + A*np.sin(2*np.pi*fre[19]*n_len) #シレファ#
            y = np.append(y, code)
        elif n=='As':
            code = A*np.sin(2*np.pi*fre[11]*n_len) + A*np.sin(2*np.pi*fre[15]*n_len) + A*np.sin(2*np.pi*fre[18]*n_len) #ラ#レファ
            y = np.append(y, code)
        elif n=='G':
            code = A*np.sin(2*np.pi*fre[8]*n_len) + A*np.sin(2*np.pi*fre[12]*n_len) + A*np.sin(2*np.pi*fre[15]*n_len) # ソシレ
            y = np.append(y, code)
        elif n=='DFs':
            code = A*np.sin(2*np.pi*fre[7]*n_len) + A*np.sin(2*np.pi*fre[10]*n_len) + A*np.sin(2*np.pi*fre[15]*n_len) #ファ#ラレ
            y = np.append(y, code)

    # メロディー
    A = 1   # 振幅

    f0=0
    f1=987.7666025122483
    f2=880.0
    f3=783.9908719634985
    f4=739.9888454232688
    f5=659.2551138257398
    f6=587.3295358348151
    f7=554.3652619537442
    f8=493.8833012561241
    f9=466.1637615180899
    f10=130.81278265

    t = (120/106) * 2/4
    n_len = np.arange(0, t, 1/rate)

    t = np.arange(0, 0.5660377358490566, 1/rate)
    t2=np.arange(0, 1.1320754716981132, 1/rate)
    t4=np.arange(0, 0.2830188679245283, 1/rate)
    t5=np.arange(0, 0.14150943396226415, 1/rate)
    t6=np.arange(0, 0.07075471698113207, 1/rate)
    t7=np.arange(0, 0.18867924528301885, 1/rate)
    t8=np.arange(0, 0.4528301886792453, 1/rate)

    z = A*np.sin(2*np.pi*f0*t2)
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t5))
    z=np.append(z,A*np.sin(2*np.pi*f4*t5))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t5))
    z=np.append(z,A*np.sin(2*np.pi*f3*t5))
    z=np.append(z,A*np.sin(2*np.pi*f4*t))
    z=np.append(z,A*np.sin(2*np.pi*f0*t))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t4))
    z=np.append(z,A*np.sin(2*np.pi*f2*t))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))#31終わり
    z=np.append(z,A*np.sin(2*np.pi*f8*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t))
    z=np.append(z,A*np.sin(2*np.pi*f0*t4))
    z=np.append(z,A*np.sin(2*np.pi*f7*t4))
    z=np.append(z,A*np.sin(2*np.pi*f7*t))
    z=np.append(z,A*np.sin(2*np.pi*f0*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f7*t5))
    z=np.append(z,A*np.sin(2*np.pi*f8*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))#34
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t5))
    z=np.append(z,A*np.sin(2*np.pi*f4*t5))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f0*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f3*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t5))
    z=np.append(z,A*np.sin(2*np.pi*f3*t5))
    z=np.append(z,A*np.sin(2*np.pi*f3*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f1*t4))
    z=np.append(z,A*np.sin(2*np.pi*f2*t4))
    z=np.append(z,A*np.sin(2*np.pi*f2*t4))
    z=np.append(z,A*np.sin(2*np.pi*f1*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t))
    z=np.append(z,A*np.sin(2*np.pi*f5*t))#37
    z=np.append(z,A*np.sin(2*np.pi*f4*t))
    z=np.append(z,A*np.sin(2*np.pi*f0*t))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t5))
    z=np.append(z,A*np.sin(2*np.pi*f4*t5))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t4))
    z=np.append(z,A*np.sin(2*np.pi*f2*t))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f8*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))#40
    z=np.append(z,A*np.sin(2*np.pi*f4*t))
    z=np.append(z,A*np.sin(2*np.pi*f0*t4))
    z=np.append(z,A*np.sin(2*np.pi*f7*t4))
    z=np.append(z,A*np.sin(2*np.pi*f7*t))
    z=np.append(z,A*np.sin(2*np.pi*f0*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f7*t5))
    z=np.append(z,A*np.sin(2*np.pi*f8*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t5))
    z=np.append(z,A*np.sin(2*np.pi*f2*t5))
    z=np.append(z,A*np.sin(2*np.pi*f2*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t8))
    z=np.append(z,A*np.sin(2*np.pi*f0*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f5*t5))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f8*t5))
    z=np.append(z,A*np.sin(2*np.pi*f8*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f0*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t4))
    z=np.append(z,A*np.sin(2*np.pi*f3*t4))
    z=np.append(z,A*np.sin(2*np.pi*f4*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f8*t4))
    z=np.append(z,A*np.sin(2*np.pi*f8*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t4))
    z=np.append(z,A*np.sin(2*np.pi*f6*t))
    z=np.append(z,A*np.sin(2*np.pi*f0*t))
    z=np.append(z,A*np.sin(2*np.pi*f0*t))
    z=np.append(z,A*np.sin(2*np.pi*f0*t))

    st.markdown('# マリーゴールド')
    st.markdown('## コード')
    st.audio(y, sample_rate=rate)
    st.markdown('## メロディー')
    st.audio(z, sample_rate=rate)

    st.markdown('## 合体')
    st.audio("output.wav", format="audio/wav") #displaying the audio

elif selector=="page2":
    y = 0
    A = 1
    fre = [0] + [440.0 * 2.0**((i-9)/12.0) for i in range(24)]
    rate = 48000
    BPM = 106

    codes = st.text_input('コードを入力', 'C D E F G A B C1')
    codes = codes.split(' ')
    if codes:
        st.write("あなたが入力したコードは: ", codes)

    note_len = st.text_input('音符を入力', '8 8 8 8 8 8 4')
    note_len = note_len.split(' ')
    if note_len:
        st.write("あなたが入力した音符は: ", note_len)

    if codes and note_len == True:
        for r,n in zip(note_len,codes):
            t = (120/BPM) * 2/r
            n_len = np.arange(0, t, 1/rate)
            if n=='R':
                code = A*np.sin(2*np.pi*fre[0]*n_len) + A*np.sin(2*np.pi*fre[0]*n_len) + A*np.sin(2*np.pi*fre[0]*n_len)
                y = np.append(y, code)
            elif n=='C':
                code = A*np.sin(2*np.pi*fre[1]*n_len) + A*np.sin(2*np.pi*fre[5]*n_len) + A*np.sin(2*np.pi*fre[8]*n_len) #ラレミ
                y = np.append(y, code)
            elif n=='C♯' or 'D♭':
                code = A*np.sin(2*np.pi*fre[2]*n_len) + A*np.sin(2*np.pi*fre[6]*n_len) + A*np.sin(2*np.pi*fre[9]*n_len)#ラド#ミ
                y = np.append(y, code)
            elif n=='D':
                code = A*np.sin(2*np.pi*fre[3]*n_len) + A*np.sin(2*np.pi*fre[7]*n_len) + A*np.sin(2*np.pi*fre[10]*n_len) #レファ#ラ
                y = np.append(y, code)
            elif n=='D♯' or 'E♭':
                code = A*np.sin(2*np.pi*fre[4]*n_len) + A*np.sin(2*np.pi*fre[8]*n_len) + A*np.sin(2*np.pi*fre[11]*n_len) #ド#ミラ
                y = np.append(y, code)
            elif n=='E':
                code = A*np.sin(2*np.pi*fre[5]*n_len) + A*np.sin(2*np.pi*fre[9]*n_len) + A*np.sin(2*np.pi*fre[12]*n_len) #シレファ#
                y = np.append(y, code)
            elif n=='F':
                code = A*np.sin(2*np.pi*fre[6]*n_len) + A*np.sin(2*np.pi*fre[10]*n_len) + A*np.sin(2*np.pi*fre[13]*n_len) #ラ#レファ
                y = np.append(y, code)
            elif n=='F♯' or 'G♭':
                code = A*np.sin(2*np.pi*fre[7]*n_len) + A*np.sin(2*np.pi*fre[11]*n_len) + A*np.sin(2*np.pi*fre[14]*n_len) # ソシレ
                y = np.append(y, code)
            elif n=='G':
                code = A*np.sin(2*np.pi*fre[8]*n_len) + A*np.sin(2*np.pi*fre[12]*n_len) + A*np.sin(2*np.pi*fre[15]*n_len) #ファ#ラレ
                y = np.append(y, code)
            elif n=='G♯' or 'A♭':
                code = A*np.sin(2*np.pi*fre[9]*n_len) + A*np.sin(2*np.pi*fre[13]*n_len) + A*np.sin(2*np.pi*fre[16]*n_len) #ラ#レファ
                y = np.append(y, code)
            elif n=='A':
                code = A*np.sin(2*np.pi*fre[10]*n_len) + A*np.sin(2*np.pi*fre[14]*n_len) + A*np.sin(2*np.pi*fre[17]*n_len) # ソシレ
                y = np.append(y, code)
            elif n=='A♯' or 'B♭':
                code = A*np.sin(2*np.pi*fre[11]*n_len) + A*np.sin(2*np.pi*fre[15]*n_len) + A*np.sin(2*np.pi*fre[18]*n_len) #ファ#ラレ
                y = np.append(y, code)
            elif n=='B':
                code = A*np.sin(2*np.pi*fre[12]*n_len) + A*np.sin(2*np.pi*fre[16]*n_len) + A*np.sin(2*np.pi*fre[19]*n_len) # ソシレ
                y = np.append(y, code)
            elif n=='B♯' or 'C♭':
                code = A*np.sin(2*np.pi*fre[13]*n_len) + A*np.sin(2*np.pi*fre[17]*n_len) + A*np.sin(2*np.pi*fre[20]*n_len) #ファ#ラレ
                y = np.append(y, code)
            elif n=='C1':
                code = A*np.sin(2*np.pi*fre[14]*n_len) + A*np.sin(2*np.pi*fre[18]*n_len) + A*np.sin(2*np.pi*fre[21]*n_len) #ファ#ラレ
                y = np.append(y, code)

        st.markdown('## 入力したコード')
        st.audio(y, sample_rate=rate)