import streamlit as st
import string

st.write("""
# TBA
Saya Akbar
while - do |
while <KONDISI> do <AKSI> endwhile
""")
def lexicalAnalyzer(kalimat):
    input_string = kalimat.lower()+'#'

    # initialization
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8',
                  'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16',
                  'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24',
                  'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32',
                  'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41']

    true = ' true'
    false = ' false'
    variable = ['a','b']
    angka = [0,1,2,3,4,5,6,7,8,9]
    simbol = ['<','>','=','!']

    transition_table = {}
    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

    try:
        #<while>
        baca_while = "while"
        for i in baca_while :
            transition_table['q0', i] = 'q0'

        #<space>
        transition_table['q0', ' '] = 'q1'

        #<variabel>
        for i in variable:
            try:
                transition_table['q1', str(i)] = 'q2'
            except:
                continue
        #<space>      
        transition_table['q2', ' '] = 'q3'

        #<operator> 
        for i in simbol:
            try:
                if i == '=' or i == '!':
                    transition_table['q3', str(i)] = 'q34'
                    for i in simbol :
                        try:
                            transition_table['q34', str(i)] = 'q4'
                        except:
                            continue                
                elif i == '<' or i == '>':
                    transition_table['q3', '<'] = 'q4'
                    transition_table['q3', '>'] = 'q4'
                    transition_table['q4', '='] = 'q4'
                else:
                    transition_table['q3', str(i)] = 'q4'
            except:
                continue
        #<space>
        transition_table['q4', ' '] = 'q5'

        #<angka>/<variabel>
        for i in angka:
            try:
                transition_table['q5', str(i)] = 'q6'
            except:
                continue
        for i in variable:
            try:
                transition_table['q5', str(i)] = 'q6'
            except:
                continue
        
        baca_do = " do "
        for i in baca_do :
            transition_table['q6', i] = 'q6'

        #<angka>/<variabel>
        for i in variable:
            try:
                transition_table['q6', str(i)] = 'q7'
            except:
                continue

        baca_samadengan = " = "
        for i in baca_samadengan :
            transition_table['q7', i] = 'q7'

        #<angka>/<variabel>
        for i in angka:
            try:
                transition_table['q7', str(i)] = 'q8'
            except:
                continue
        for i in variable:
            try:
                transition_table['q7', str(i)] = 'q8'
            except:
                continue
        
        baca_kali = " * "
        for i in baca_kali :
            transition_table['q8', i] = 'q8'

        #<angka>/<variabel>
        for i in angka:
            try:
                transition_table['q8', str(i)] = 'q9'
            except:
                continue
        for i in variable:
            try:
                transition_table['q8', str(i)] = 'q9'
            except:
                continue
        
        baca_endwhile = " endwhile"
        for i in baca_endwhile:
            transition_table['q9', i] = 'q9'
        transition_table['q9', '#'] = 'accept'
    except:
        return false

 
    # lexical analisis
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'q41':
            # print('current token :',current_token,', valid')
            return True
            current_token = ''
        if state == 'error':
            # print('error')
            return False
            break
        idx_char = idx_char + 1

    if state == 'accept':
        # print('semua token di input:', sentence, ', valid')
        return True

hasil = st.text_input("Hasil Code","while a < 1 do a = a * b endwhile")
if lexicalAnalyzer(hasil) :
    st.success("Anda Benar")
else:
    st.success("Kamu Salah")

hasil = hasil.split(" ")
parser = False
if hasil[0] == "while" :
    if hasil[2] == "do":
        parser = True

kalimat = "while i<1"
#st.success(hasil)
#st.success(kalimat)
#st.success(lexicalAnalyzer(kalimat))
st.text(" Grammar: \n<statement> ::= if <kondisi> then <aksi> endif \n<kondisi> ::= <variabel> <operator> <variabel>\n<kondisi> ::= true | false\n<aksi> ::= <variabel> = <variabel> * <variabel>\n<variabel> ::= a | b \n<operator> ::= == | >= | <= | < | >")