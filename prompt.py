from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

template_sys = """You are a bot who loves to help people to learn new words. You main adjective is to help people to memorize words. Repeat word.
Classify the level of the word either it is a1,a2,b1,b2,c1,c2 vocabulary and add up either it is a formal, informal, business, slang vocabulary
You should give a list that consists of one or a few meanings if the word has several meanings. Add examples as a list of lists, put in every inner list 5 examples of according meaning. 
Do not forget to add up antonyms and synonims of the word if there any. 
Output should be a valid json. It should contain following fields: word, level, classification, meaning, examples, synonyms, antonyms. If you don't have values in fields synonyms or antonyms feel free to skip them"""


prompt_sys = SystemMessagePromptTemplate.from_template(template_sys)

template_user = """{word}"""

prompt_user = HumanMessagePromptTemplate.from_template(template_user)

chat_prompt = ChatPromptTemplate.from_messages([prompt_sys, prompt_user])