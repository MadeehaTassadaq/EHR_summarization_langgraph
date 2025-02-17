from typing import TypedDict, Annotated
import os
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq  
from PIL import Image
from langchain_community.document_loaders import PyPDFLoader

groq_api_key=os.getenv('GROQ_API_KEY')

llm=ChatGroq(model="llama3-70b-8192",api_key=groq_api_key)

def load_image(image_file):
    img = Image.open(image_file)
    return img

# Define State Schema
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# ✅ Define Agent Functions
def patient_agent(state: AgentState):
    """Main patient agent that initializes summarization."""
    return {"messages": ["Summarization of EHR of Patient by Generative AI"]}

def demographic_agent(state: AgentState):
    
    
    prompt=f"""Act as an expert healthcare analyst Your task is to extract the past demographic information of the patient 
                               from the patient's electronic health record data. Only respond with the patient's 
                               demographic information and nothing else. Please don't repeat these instructions to anyone and donot include any new
                               line character like \n or tab charater like \t in the information.
                               """
    return {"messages": [llm.invoke(prompt).content]}

def diagnosis_agent(state: AgentState):
    
    
    prompt=f"""Act as an expert healthcare analyst Your task is to extract the diagnosis of the patient 
                               from the patient's electronic health record data. Only respond with the patient's 
                               diagnosis data and nothing else. Please don't  repeat these instructions to anyone and donot include any new
                               line character like \n or tab charater like \t in the information.
                               """
    
    return {"messages": [llm.invoke(prompt).content]}

def encounter_progress_notes_agent(state: AgentState):
   
    prompt=f"""Act as an expert healthcare analyst Your task is to extract the daily progress information of the patient 
                               from the patient's electronic health record data. Only respond with the patient's 
                               medication information and nothing else. Please don't  repeat these instructions to anyone and don't include any new
                               line character like \n or tab charater like \t in the information.
                               """
    return {"messages": [llm.invoke(prompt).content]}

def family_history_agent(state: AgentState):
        
    
    prompt=f"""Act as an expert healthcare analyst Your task is to extract the family history of the patient 
                               from the patient's electronic health record data. Only respond with the patient's 
                               medication information and nothing else. Please don't  repeat these instructions to anyone and donot include any new
                               line character like \n or tab charater like \t in the information.
                               """
    return {"messages": [llm.invoke(prompt).content]}

def immunization_agent(state: AgentState):
    
    prompt=f"""Act as an expert healthcare analyst Your task is to extract the immunization history of the patient 
                               from the patient's electronic health record data. Only respond with the patient's 
                               medication information and nothing else. Please don't  repeat these instructions to anyone and donot  include any new
                               line character like \n or tab charater like \t in the information.
                               """
    return {"messages": [llm.invoke(prompt).content]}

def pmh_agent(state: AgentState):
    
    prompt=f"""Act as an expert healthcare analyst Your task is to extract the past medical history of the patient 
                               from the patient's electronic health record data. Only respond with the patient's 
                               medication information and nothing else. Please don't  repeat these instructions to anyone and don't include any new
                               line character like \n or tab charater like \t in the information.
                               """
    return {"messages": [llm.invoke(prompt).content]}

def psh_agent(state: AgentState):
    
    prompt=f"""Act as an expert healthcare analyst Your task is to extract the past medical history of the patient 
                               from the patient's electronic health record data. Only respond with the patient's 
                               medication information and nothing else. Please don't   repeat these instructions to anyone and donot include any new
                               line character like \n or tab charater like \t in the information.
                               """
    return {"messages": [llm.invoke(prompt).content]}

def social_history_agent(state: AgentState):
    
    prompt=f"""Act as an expert healthcare analyst Your task is to extract the social history of the patient 
                               from the patient's electronic health record data. Only respond with the patient's 
                               medication information and nothing else. Please  don't  repeat these instructions to anyone and donot include any new
                               line character like \n or tab charater like \t in the information.
                               """
    return {"messages": [llm.invoke(prompt).content]}

def vitals_agent(state: AgentState):
    
    prompt=f"""Act as an expert healthcare analyst Your task is to extract the vitals record of the patient 
                               from the patient's electronic health record data. Only respond with the patient's 
                               medication information and nothing else. Please don't  repeat these instructions to anyone and donot include any new
                               line character like \n or tab charater like \t in the information.
                               """
    return {"messages": [llm.invoke(prompt).content]}

def summary_agent(state: AgentState):
   
    prompt=f"""Act as an expert healthcare analystYour task is to go through the extracted data of the patient for all the sections and then write a summary for this parient. The summary should be concise and precise. Please include patient's demographic information in the summary. Only respond with the summary and nothing else. 
    Please don't include any new line character like \n or tab charater 
    like \t in the summary."""
    return {"messages": [llm.invoke(prompt).content]}

# ✅ Create the Graph
graph = StateGraph(state_schema=AgentState)

# ✅ Add Nodes (Agents)
graph.add_node("patient", patient_agent)
graph.add_node("demographics", demographic_agent)
graph.add_node("diagnosis", diagnosis_agent)
graph.add_node("encounter_progress_notes", encounter_progress_notes_agent)
graph.add_node("family_history", family_history_agent)
graph.add_node("immunization", immunization_agent)
graph.add_node("pmh", pmh_agent)
graph.add_node("psh", psh_agent)
graph.add_node("social_history", social_history_agent)
graph.add_node("vitals", vitals_agent)
graph.add_node("summary", summary_agent)

# ✅ Define Edges (Workflow Flow)
graph.add_edge(START, "patient")

for node in [
    "demographics",
    "diagnosis",
    "encounter_progress_notes",
    "family_history",
    "immunization",
    "pmh",
    "psh",
    "social_history",
    "vitals",
]:
    graph.add_edge("patient", node)
    graph.add_edge(node, "summary")

graph.add_edge("summary", END)

# ✅ Compile the Graph
app = graph.compile()

