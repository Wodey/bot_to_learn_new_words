from typing import Any
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from prompt import chat_prompt
from word import Word
import logging

load_dotenv()


class Model():
    def __init__(self) -> None:
        self.chat = ChatOpenAI(temperature=0)
        self.parser = PydanticOutputParser(pydantic_object=Word)
    
    def __call__(self, word) -> Any:
        res = self.chat(chat_prompt.format_messages(word=word))

        try:
            parser_res = self.parser.parse(res.content)
            return parser_res
        except:
            logging.error('There is a error with output of the model, try again')
        

        
if __name__ == '__main__':
    bot = Model()
    print(bot('again'))