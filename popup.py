from streamlit_modal import Modal
import streamlit.components.v1 as components
import streamlit as st

def popup(title, content):
    modal = Modal("Demo Modal", key="sdfsdfs")
    open_modal = st.button("Open")
    if open_modal:
        modal.open()
    if modal.is_open():
        with modal.container():
            html_string = f'''
            <script language="javascript">
              document.querySelector("div h1").style.color = "red";
            </script>
            <style>
              .color-green {{
                color: green;
              }}
            </style>
            <div >
                <h1 class="color-green">{title}</h1>
                <p>{content}</p>
            </div>
            '''
            components.html(html_string)
            # value = st.checkbox("Check me")
            # st.write(f"Checkbox checked: {value}")

