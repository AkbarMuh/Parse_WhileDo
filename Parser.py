import streamlit as st
import string
import pandas as pd
import numpy as np

st.write("""
# TBA - Parser 'while do' in Python 
Kelompok 4 | while <KONDISI> : <AKSI>
""")
st.text("while <KONDISI>:\n     <AKSI>")

def lexicalAnalyzer(kalimat):
    input_string = str(kalimat.lower()+' #')

    # initialization
    list_input = list(string.ascii_lowercase)
    list_state = ['q0','q00', 'q01', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8',
                  'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16',
                  'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24',
                  'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32',
                  'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 
                  'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48',
                  'q49', 'q50', 'q51', 'q52', 'q53', 'q54', 'q55', 'q56']

    variable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    arithmetic = ['+','-','*','/','%']
    angka = ['0','1','2','3','4','5','6','7','8','9']
    simbol = ['<','>','=','!']

    tabel_transisi = {}
    for state in list_state:
        for alphabet in list_input:
            tabel_transisi[(state, alphabet)] = 'error'
        tabel_transisi[(state, '#')] = 'error'
        tabel_transisi[(state, ' ')] = 'error'

    # kalo ada spasi sebelum input
    tabel_transisi['q0', ' '] = 'q0'

    #<while>
    tabel_transisi['q0', 'w'] = 'q00'
    tabel_transisi['q00', 'h'] = 'q01'
    tabel_transisi['q01', 'i'] = 'q00'
    tabel_transisi['q00', 'l'] = 'q01'
    tabel_transisi['q01', 'e'] = 'q0'

    #<space>
    tabel_transisi['q0', ' '] = 'q1'
    
    #<variabel>
    for i in variable:
        tabel_transisi['q1', str(i)] = 'q2'

    #<True>
    tabel_transisi['q1', 't'] = 'q32'
    tabel_transisi['q32', 'r'] = 'q31'
    tabel_transisi['q31', 'u'] = 'q32'
    tabel_transisi['q32', 'e'] = 'q31'
    tabel_transisi['q31', ' '] = 'q7'
    #<False>
    tabel_transisi['q1', 'f'] = 'q32'
    tabel_transisi['q32', 'a'] = 'q31'
    tabel_transisi['q31', 'l'] = 'q32'
    tabel_transisi['q32', 's'] = 'q31'
    tabel_transisi['q31', 'e'] = 'q32'
    tabel_transisi['q32', ' '] = 'q7'

    #<space>      
    tabel_transisi['q2', ' '] = 'q3'

    #<operator> 
    for i in simbol:
        if i == '=' or i == '!':
            tabel_transisi['q3', str(i)] = 'q34'
            for i in simbol :
                tabel_transisi['q34', str(i)] = 'q4'                
        elif i == '<' or i == '>':
            tabel_transisi['q3', '<'] = 'q4'
            tabel_transisi['q3', '>'] = 'q4'
            tabel_transisi['q4', '='] = 'q4'
        else:
            tabel_transisi['q3', str(i)] = 'q4'

    #<space>
    tabel_transisi['q4', ' '] = 'q5'

    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q5', str(i)] = 'q6'
    for i in variable:
        tabel_transisi['q5', str(i)] = 'q6'
    
    #<space>
    tabel_transisi['q6', ' '] = 'q7'
    
    #<do>
    tabel_transisi['q7', 'd'] = 'q8'
    tabel_transisi['q7', ':'] = 'q9'
    tabel_transisi['q8', 'o'] = 'q9'

    #<space>
    tabel_transisi['q9', ' '] = 'q10'
    tabel_transisi['q10', ' '] = 'q10'

    #<variabel>
    for i in variable:
        tabel_transisi['q10', str(i)] = 'q11'

    tabel_transisi['q10', 'p'] = 'q41'
    tabel_transisi['q41', 'r'] = 'q42'
    tabel_transisi['q42', 'i'] = 'q43'
    tabel_transisi['q43', 'n'] = 'q44'
    tabel_transisi['q44', 't'] = 'q45'
    tabel_transisi['q45', '('] = 'q47'

    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q47', str(i)] = 'q48'
    for i in variable:
        tabel_transisi['q47', str(i)] = 'q48'
    
    tabel_transisi['q48', ')'] = 'q49'
    tabel_transisi['q49', ' '] = 'q50'
    tabel_transisi['q50', '#'] = 'accept'
    tabel_transisi['q50', ' '] = 'q10'
    
    #<space>
    tabel_transisi['q11', ' '] = 'q12'

    #< = >
    tabel_transisi['q12', '='] = 'q13'

    #<space>
    tabel_transisi['q13', ' '] = 'q14'

    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q14', str(i)] = 'q15'
    for i in variable:
        tabel_transisi['q14', str(i)] = 'q15'
    
    #<space>
    tabel_transisi['q15', ' '] = 'q16'

    #<arithmetic>
    for i in arithmetic:
        if i == '/' or i == '*' :
            tabel_transisi['q16', i] = 'q17'
            tabel_transisi['q17', i] = 'q17'
        tabel_transisi['q16', i] = 'q17'

    #<space>
    tabel_transisi['q17', ' '] = 'q18'
    
    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q18', str(i)] = 'q19'
    for i in variable:
        tabel_transisi['q18', str(i)] = 'q19'
    
    #<space + #>
    tabel_transisi['q19', ' '] = 'q20'
    tabel_transisi['q20', '#'] = 'accept'
    tabel_transisi['q20', ' '] = 'q10'
    
    # lexical analisis\
    st.write("""
    ##### Hasil Parse
    """)
    n =  0
    idx_char = 0
    state = 'q0'
    token_ygSekarang = ''
    while state != 'accept':
        titik_Sekarang = input_string[idx_char]
        token_ygSekarang += titik_Sekarang
        state = tabel_transisi[(state, titik_Sekarang)]
        #   st.write(n, input_string[idx_char])
        n = n+1
        if state == 'error':
            return False
        idx_char = idx_char + 1
    if state == 'accept':
        return True

def ParserAnalyzer(kalimat,Parser,FA):
    input_string = str(kalimat.lower()+' #')

    # initialization
    list_input = list(string.ascii_lowercase)
    list_state = ['q0','q00', 'q01', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8',
                  'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16',
                  'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24',
                  'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32',
                  'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 
                  'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48',
                  'q49', 'q50', 'q51', 'q52', 'q53', 'q54', 'q55', 'q56']

    variable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    arithmetic = ['+','-','*','/','%']
    angka = ['0','1','2','3','4','5','6','7','8','9']
    simbol = ['<','>','=','!']

    tabel_transisi = {}
    for state in list_state:
        for alphabet in list_input:
            tabel_transisi[(state, alphabet)] = 'error'
        tabel_transisi[(state, '#')] = 'error'
        tabel_transisi[(state, ' ')] = 'error'

    # kalo ada spasi sebelum input
    tabel_transisi['q0', ' '] = 'q0'

    #<while>
    tabel_transisi['q0', 'w'] = 'q00'
    tabel_transisi['q00', 'h'] = 'q01'
    tabel_transisi['q01', 'i'] = 'q00'
    tabel_transisi['q00', 'l'] = 'q01'
    tabel_transisi['q01', 'e'] = 'q1'

    #<space>
    tabel_transisi['q1', ' '] = 'q1'
    
    #<variabel>
    for i in variable:
        tabel_transisi['q1', str(i)] = 'q2'

    #<True>
    tabel_transisi['q1', 't'] = 'q32'
    tabel_transisi['q32', 'r'] = 'q31'
    tabel_transisi['q31', 'u'] = 'q32'
    tabel_transisi['q32', 'e'] = 'q31'
    tabel_transisi['q31', ' '] = 'q6'
    #<False>
    tabel_transisi['q1', 'f'] = 'q32'
    tabel_transisi['q32', 'a'] = 'q31'
    tabel_transisi['q31', 'l'] = 'q32'
    tabel_transisi['q32', 's'] = 'q31'
    tabel_transisi['q31', 'e'] = 'q32'
    tabel_transisi['q32', ' '] = 'q6'

    #<space>      
    tabel_transisi['q2', ' '] = 'q2'

    #<operator> 
    for i in simbol:
        if i == '=' or i == '!':
            tabel_transisi['q2', str(i)] = 'q34'
            for i in simbol :
                tabel_transisi['q34', str(i)] = 'q4'                
        elif i == '<' or i == '>':
            tabel_transisi['q2', '<'] = 'q4'
            tabel_transisi['q2', '>'] = 'q4'
            tabel_transisi['q4', '='] = 'q4'
        else:
            tabel_transisi['q2', str(i)] = 'q4'

    #<space>
    tabel_transisi['q4', ' '] = 'q4'

    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q4', str(i)] = 'q6'
    for i in variable:
        tabel_transisi['q4', str(i)] = 'q6'
    
    #<space>
    tabel_transisi['q6', ' '] = 'q6'
    
    #<do>
    tabel_transisi['q6', 'd'] = 'q8'
    tabel_transisi['q6', ':'] = 'q9'
    tabel_transisi['q8', 'o'] = 'q9'

    #<space>
    tabel_transisi['q9', ' '] = 'q10'
    tabel_transisi['q10', ' '] = 'q10'

    #<variabel>
    for i in variable:
        tabel_transisi['q10', str(i)] = 'q11'

    tabel_transisi['q10', 'p'] = 'q41'
    tabel_transisi['q41', 'r'] = 'q42'
    tabel_transisi['q42', 'i'] = 'q43'
    tabel_transisi['q43', 'n'] = 'q44'
    tabel_transisi['q44', 't'] = 'q45'
    tabel_transisi['q45', ' '] = 'q45'
    tabel_transisi['q45', '('] = 'q47'

    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q47', str(i)] = 'q48'
    for i in variable:
        tabel_transisi['q47', str(i)] = 'q48'
    
    tabel_transisi['q48', ')'] = 'q49'
    tabel_transisi['q49', ' '] = 'q50'
    tabel_transisi['q50', '#'] = 'accept'
    tabel_transisi['q50', ' '] = 'q10'
    
    #<space>
    tabel_transisi['q11', ' '] = 'q12'

    #< = >
    tabel_transisi['q12', '='] = 'q13'

    #<space>
    tabel_transisi['q13', ' '] = 'q14'

    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q14', str(i)] = 'q15'
    for i in variable:
        tabel_transisi['q14', str(i)] = 'q15'
    
    #<space>
    tabel_transisi['q15', ' '] = 'q16'

    #<arithmetic>
    for i in arithmetic:
        if i == '/' or i == '*' :
            tabel_transisi['q16', i] = 'q17'
            tabel_transisi['q17', i] = 'q17'
        tabel_transisi['q16', i] = 'q17'

    #<space>
    tabel_transisi['q17', ' '] = 'q18'
    
    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q18', str(i)] = 'q19'
    for i in variable:
        tabel_transisi['q18', str(i)] = 'q19'
    
    #<space + #>
    tabel_transisi['q19', ' '] = 'q20'
    tabel_transisi['q20', '#'] = 'accept'
    tabel_transisi['q20', ' '] = 'q10'
    
    # lexical analisis\
    idx_char = 0
    state = 'q0'
    token_ygSekarang = ''
    while state != 'accept':
        titik_Sekarang = input_string[idx_char]
        token_ygSekarang += titik_Sekarang
        state = tabel_transisi[(state, titik_Sekarang)]
        if FA[:-1] != state:
            if titik_Sekarang == ' ' : Parser.append('space')
            else: Parser.append(titik_Sekarang)
            FA.append(state)
        if state == 'error':
            return False, Parser, FA
        idx_char = idx_char + 1
    if state == 'accept':
        return True, Parser, FA

css = r'''
    <style>
        [data-testid="stForm"] {border: 0px}
    </style>
'''
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77701389101.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url() 


# st.write("""
# ##### Parsing Code 1 Line
# """)

# with st.form("my_form"):
#    hasil = st.text_input("Copas Hasil Code Kesini (1 Line)","while a < 1 : a = a * b")
#    submitted = st.form_submit_button("Ini Tombol Submit")
# try:
#     if lexicalAnalyzer(hasil) :
#         st.success("Anda Benar")
#     else:
#         st.success("Kamu Salah")
# except:
#     st.success("Kamu Jelek")

# st.text("\n")


st.write("""
##### Parsing Code Umum
""")
Parser = []
FA = []
with st.form("my_form2"):   
    txt = st.text_area("Copas Code kesini", "while a < 1 :\n     print(a)\n     a = b + c")
    txt = txt.replace("\n",'')
    submitted = st.form_submit_button("Ini Tombol Submit")
try:
    if ParserAnalyzer(txt, Parser, FA)[0] :
        st.success("Anda Benar")
    else:
        st.success("Kamu Salah")
except:
    st.success("Kamu Salah")

st.write("""
##### Hasil Parse
""")

list_of_tuples = list(zip(FA, Parser))
df = pd.DataFrame(
    list_of_tuples, columns=['State', 'Parse']
    )
st.table(df)

# i = 0
# for i in range(len(FA)):
#     st.write(i,FA[i], Parser[i])
# a = Parser[0]
# for i in Parser[1:-1]:
#     if i != 'space' :
#         a = a + i 
#     else: a = a + " <space> "
# st.markdown(a)



st.text(" Grammar: \n<statement> ::= while <kondisi> : <aksi> endwhile \n<kondisi> ::= <variabel> <operator> <variabel/angka>\n<kondisi> ::= true | false\n<aksi> ::= <variabel> = <variabel/angka> <arithmetic> <variabel/angka>\n<aksi> ::= print(<variabel/angka>)\n<variabel> ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z\n<angka> ::= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 \n<arithmetic> ::= + | - | * | / | % | ** | //\n<operator> ::= == | >= | <= | < | > | != | ==")
