from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_models import ChatOllama

from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import google.generativeai as genai
import streamlit as st
import os,io,glob
from dotenv import load_dotenv


load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
st.title("CLOUD ARCHITECTURE DIAGRAM APP")
st.write("create any diagram of your choice")
input=st.text_area("ask anything about your task")

ts="""
Your job is to write the python code using Diagram module to generate cloud archtecture diagrm for
    {steps} information only , dont use any other information.
    only generate the code as output nothing extra.
    for reference use below :
    to import ELB  in the code always use below
    from diagrams.aws.network import ELB
    check code twice that code is working
    Code:
    """
pt=ChatPromptTemplate.from_template(ts)
llm = ChatGoogleGenerativeAI(model="gemini-pro")
qa_chain=LLMChain(llm=llm,prompt=pt)

if input is not None:
    btn=st.button("submit")
    if btn:
        response=qa_chain.invoke({"steps":input})
        data=response["text"]
        code=data.replace("python","")
        code=code.replace("`","")
        cwd=os.getcwd()
        files=glob.glob(cwd+"/*.png")
        for file in files:
            os.remove(file)
        with io.open("codesample.py","w",encoding="utf-8")as f1:
            f1.write(code)
            f1.close()
        os.system("python codesample.py")
        files=glob.glob(cwd+"/*.png")
        print(files)
        if len(files)==1:
            st.image(files)