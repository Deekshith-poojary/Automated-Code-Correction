import getpass
import os,json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
import template,helper,update_file
import error_extracter as ex

#use any one from the below services
os.environ["GOOGLE_API_KEY"] ="YUUR_GOOGLE_API_KEY"
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
temp,ls,le=helper.getcode(helper.file_path)

prompt=template.prompt2.invoke({"code_snippet":temp,"ls":ls,"le":le})
inputs = {"messages":str(prompt)}

final_answer=None
for s in graph.stream(inputs, stream_mode="values"):
    message = s["messages"][-1]
    if hasattr(message, "content"):  # Check if it's an AIMessage or similar
        # Update the final_answer with the latest AIMessage content
        final_answer = message.content

final_answer=str(final_answer)

json_string = final_answer.strip().replace('```json\n', '').replace('```', '')

json_data = json.loads(json_string)
update_file.update_file_with_corrections(helper.file_path,json_data)
