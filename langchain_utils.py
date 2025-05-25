from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import json



def load_prompt_template(filepath: str) -> PromptTemplate:
    with open(filepath, 'r') as f:
        prompt_json = json.load(f)
    return PromptTemplate(
        input_variables=prompt_json["input_variables"],
        template=prompt_json["template"]
    )

def generate_schedule_db(output):
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")

    # Initialize the OpenAI chat model
    model = ChatOpenAI(model="gpt-4.1", temperature=0.3, api_key=api_key)

    file_path = os.path.join(os.path.dirname(__file__), "study_prompt_db.json")
    list_format_prompt = load_prompt_template(file_path)


    db_chain = list_format_prompt | model

    formatted_db_output = db_chain.invoke({"output": output}).content

    return formatted_db_output



def generate_schedule(mood, study_time, busyness, learning_topic, daily_schedule):
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")

    # Initialize the OpenAI chat model
    model = ChatOpenAI(model="gpt-4.1", temperature=0.3, api_key=api_key)

    #Getting the template
    file_path = os.path.join(os.path.dirname(__file__), "study_prompt.json")
    study_template = load_prompt_template(file_path)

    chain = study_template | model

    output = chain.invoke({
    "mood": mood,
    "study_time": study_time,
    "busyness": busyness,
    "learning_topic": learning_topic,
    "daily_schedule": daily_schedule   # <- match prompt here
}).content
    
    formatted_db_output = generate_schedule_db(output)
    print(formatted_db_output)

    print(type(formatted_db_output))

    print(formatted_db_output.strip())



    return {
        "full_schedule": output,
        "db_ready_schedule": formatted_db_output
    }



    
