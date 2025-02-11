import getpass
import os,json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
import template
import error_extracter as ex

#use any one from the below services
os.environ["GOOGLE_API_KEY"] ="YUUR_GOOGLE_GEMINAI_API_KEY"
#os.environ["OPENAI_API_KEY"]="YOUR_OPENAI_API_KEY"
#os.environ["ANTHROPIC_API_KEY"] = "YOUR_CLUAD_ANTHROPIC_API_KEY"

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.6,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

#if you want to add tool you can include here.
tools = []

graph = create_react_agent(model, tools=tools)

temp=ex.extract_new_errors(ex.logfile_path)
if temp:
    prompt=template.prompt1.invoke({"error_message":temp})
    inputs = {"messages":str(prompt)}
    print("Loading into LLM.....")
    final_answer=None
    for s in graph.stream(inputs, stream_mode="values"):
        message = s["messages"][-1]
        if hasattr(message, "content"):  # Check if it's an AIMessage or similar
            # Update the final_answer with the latest AIMessage content
            final_answer = message.content
    final_answer=str(final_answer)
