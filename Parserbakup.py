import streamlit as st
import string

st.write("""
# TBA
Saya Akbar
while - do |
while <KONDISI> do <AKSI> endwhile
""")
def lexicalAnalyzer(kalimat):
    input_string = str(kalimat.lower()+'#')

    # initialization
    list_input = list(string.ascii_lowercase)
    list_state = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8',
                  'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16',
                  'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24',
                  'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32',
                  'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41']

    variable = ['a','b']
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
    baca_while = "while"
    for i in baca_while :
        tabel_transisi['q0', i] = 'q0'

    #<space>
    tabel_transisi['q0', ' '] = 'q1'
    
    #<variabel>
    for i in variable:
        tabel_transisi['q1', str(i)] = 'q2'

    
    #<True/False>
    tabel_transisi['q1', 't'] = 'q12'
    tabel_transisi['q12', 'r'] = 'q11'
    tabel_transisi['q11', 'u'] = 'q12'
    tabel_transisi['q12', 'e'] = 'q11'
    tabel_transisi['q11', ' '] = 'q6'

    tabel_transisi['q1', 'f'] = 'q12'
    tabel_transisi['q12', 'a'] = 'q11'
    tabel_transisi['q11', 'l'] = 'q12'
    tabel_transisi['q12', 's'] = 'q11'
    tabel_transisi['q11', 'e'] = 'q12'
    tabel_transisi['q12', ' '] = 'q6'

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
    
    #< do >
    baca_do = " do "
    for i in baca_do :
        tabel_transisi['q6', i] = 'q6'

    #<variabel>
    for i in variable:
        tabel_transisi['q6', str(i)] = 'q7'

    #< = >
    baca_samadengan = " = "
    for i in baca_samadengan :
        tabel_transisi['q7', i] = 'q7'

    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q7', str(i)] = 'q8'
    for i in variable:
        tabel_transisi['q7', str(i)] = 'q8'
    
    #< * >
    baca_kali = " * "
    for i in baca_kali :
        tabel_transisi['q8', i] = 'q8'
    
    #<angka>/<variabel>
    for i in angka:
        tabel_transisi['q8', str(i)] = 'q9'
    for i in variable:
        tabel_transisi['q8', str(i)] = 'q9'
    
    #<space>
    tabel_transisi['q9', ' '] = 'q10'

    baca_endwhile = "endwhile"
    for i in baca_endwhile:
        tabel_transisi['q10', i] = 'q10'
    tabel_transisi['q10', '#'] = 'accept'
 
    # lexical analisis
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = tabel_transisi[(state, current_char)]
        if state == 'error':
            return False
            break
        idx_char = idx_char + 1
    if state == 'accept':
        return True

hasil = st.text_input("Hasil Code","while a < 1 do a = a * b endwhile")
try:
    if lexicalAnalyzer(hasil) :
        st.success("Anda Benar")
    else:
        st.success("Kamu Salah")
except:
    st.success("Kamu Salah")
 
st.text(" Grammar: \n<statement> ::= if <kondisi> then <aksi> endif \n<kondisi> ::= <variabel> <operator> <variabel>\n<kondisi> ::= true | false\n<aksi> ::= <variabel> = <variabel> * <variabel>\n<variabel> ::= a | b \n<operator> ::= == | >= | <= | < | >")
