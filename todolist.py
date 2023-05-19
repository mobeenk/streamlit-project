import streamlit as st

if  'mylist' not in st.session_state:
    mylist = []

# st.session_state.i = "A"
if  'index' not in st.session_state:
    st.session_state['index'] =0

def main():



    btn = st.button("add:")
    if btn:
        mylist.append(st.session_state['index']+1)
        # mylist.append(st.session_state.i+"1")

    def get_new_values_list():
        st.write(st.session_state['issue'])


    values = st.multiselect('issue', mylist, mylist, key='issue')
    st.write(values) # < returns correct list

main()