import streamlit as st
import string

st.write("""
# TBA - Parser 'while do' in Python 
Saya AkbarMuh | while <KONDISI> : <AKSI>
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
                  'q49', 'q50']

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
 
    # lexical analisis
    idx_char = 0
    state = 'q0'
    token_ygSekarang = ''
    while state != 'accept':
        titik_Sekarang = input_string[idx_char]
        token_ygSekarang += titik_Sekarang
        state = tabel_transisi[(state, titik_Sekarang)]
        if state == 'error':
            return False
        idx_char = idx_char + 1
    if state == 'accept':
        return True

hasil = st.text_input("Copas Hasil Code Kesini (1 Line)","while a < 1 : a = a * b")
try:
    if lexicalAnalyzer(hasil) :
        st.success("Anda Benar")
    else:
        st.success("Kamu Salah")
except:
    st.success("Kamu Jelek")

txt = st.text_area("Test Kalo Code beda line", "while a < 1 :\n     a = a * b")
txt = txt.replace("\n",'')

try:
    if lexicalAnalyzer(txt) :
        st.success("Anda Benar")
    else:
        st.success("Kamu Salah")
except:
    st.success("Kamu Jelek")
 
st.text(" Grammar: \n<statement> ::= while <kondisi> : <aksi> endwhile \n<kondisi> ::= <variabel> <operator> <variabel>\n<kondisi> ::= true | false\n<aksi> ::= <variabel> = <variabel> <arithmetic> <variabel>\n<variabel> ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z \n<arithmetic> ::= + | - | * | / | % | ** | //\n<operator> ::= == | >= | <= | < | > | != | ==")
