

from PROMPT_TEMPLATE  import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from  langchain.prompts import ChatPromptTemplate
from data_format import data_format
import os


def generate_xiaohongshu(theme, deepseek_api_key):

    prompt=ChatPromptTemplate.from_messages(
        [
            ("system",system_template_text),
            ("user",user_template_text)
        ]
    )

    model = ChatOpenAI(model='deepseek-chat', base_url='https://api.deepseek.com/v1', api_key=deepseek_api_key)

    output_parser=PydanticOutputParser (pydantic_object=data_format)

    chain=prompt | model |output_parser

    result=chain.invoke(
        {
            "parser_instructions":output_parser.get_format_instructions(),
            "theme":theme
        }
    )

    return result

#print(generate_xiaohongshu("大模型",os.getenv("deepseekapikey")))






