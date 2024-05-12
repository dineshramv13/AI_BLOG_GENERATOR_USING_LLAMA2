import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def getllamaresponse(input_text,no_words,blog_style):

    llm = CTransformers(model = 'models\llama-2-7b-chat.ggmlv3.q4_0.bin',
                        model_type = 'llama',
                        config={'max_new_tokens':256,
                                'temperature': 0.01})


    template = '''
                Write a blog for {blog_style} job profile for a topic {input_text}
                within {no_words} words.
                '''

    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title = 'AI POWERED BLOGS',
layout = 'centered',
initial_sidebar_state = "collapsed")


st.header("BLOGSSSSSSSSSS")

input_text = st.text_input("Enter the topic to create a blog")

col1 , col2   = st.columns([5,5])

with col1:
    no_words = st.text_input("no. of words")

with col2:
    blog_style = st.selectbox('writing the bolg for ', 
    ('Reasearchers' , 'Data scienctist' , 'Common people'), index = 0)


submit = st.button('GENERATEEEEEEE !!!!')

if submit:
    st.write(getllamaresponse(input_text,no_words,blog_style))
