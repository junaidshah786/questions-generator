# from langchain.vectorstores import Chroma
import streamlit as st  # import the Streamlit library

# from langchain import OpenAI,VectorDBQA
# import magic
# from langchain.text_splitter import CharacterTextSplitter
# import os
# from io import StringIO
# import nltk
# from langchain.vectorstores import FAISS
# from langchain.document_loaders import TextLoader
# import faiss
# from langchain.document_loaders import DirectoryLoader
# from langchain.embeddings.openai import OpenAIEmbeddings


st.title("`kashmir Search`")
st.header('please fill the below details')

# passage
passage=st.text_area(label='Enter your `Passage`', value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None,  placeholder='Eg: passage goes here', disabled=False, label_visibility="visible")

# radio button
# it returns the number chosen
qNos = st.radio(
    "Choose `number` of Options:",
    ('Two', 'Three','Four','Five'),horizontal=True,index=3)

if qNos is not None:
    if qNos == 'Two':
        st.success('You selected two')
    elif qNos == 'Three':
        st.success("You Selected Three")
    elif qNos == 'Four':
        st.success("You Selected Four")
    elif qNos == 'Five':
        st.success("You Selected Five")



# Grade

grade = st.selectbox(
    'Enter the `grade`:',
    ('1st', '2nd', '3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th'),index=0,help="Select the class grade for generating Questions")

st.success('Grade selected: '+ grade)
    

# difficulty

difficulty = st.radio(
    "Choose `Difficulty`:",
    ('Easy', 'Medium','hard'),horizontal=True,index=1)

if difficulty is not None:
    if difficulty == 'Easy':
        st.success('You selected Easy')
    elif difficulty == 'Medium':
        st.success("You Selected Medium")
    elif difficulty == 'hard':
        st.success("You Selected hard")


# marks

marks=st.number_input(label="Enter `marks` per Question: ", min_value=1, max_value=None, value=1, step=1, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
st.success('You choose: '+str(marks))

# Questions to be Excluded
if 'option' not in st.session_state:
    st.session_state.option=[]
if 'added' not in st.session_state:
        st.session_state.added=[]



exclude=st.text_area(label='Enter Questions to be `Excluded`: ', value="", height=None, max_chars=None, key="questions", help=None, on_change=None, args=None, kwargs=None,  placeholder='Eg: how to avoid being taken by surprise by something?', disabled=False, label_visibility="visible")
addQuestion=st.button(label="add", key=None, help=None, on_click=None, args=None, kwargs=None,  type="secondary", disabled=False, use_container_width=False)
if addQuestion:
    st.session_state.option.append(exclude)
    st.session_state.added.append(exclude)
    exclude=''
    

selectedQ = st.multiselect(
        'Select the questions you want to `Excude`',
        st.session_state.option, st.session_state.added )
st.session_state.added=selectedQ

st.button(label="Submit", key=None, help=None, on_click=None, args=None, kwargs=None,  type="primary", disabled=False, use_container_width=True)