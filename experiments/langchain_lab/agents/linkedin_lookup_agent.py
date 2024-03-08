"""Linkedin lookup agent.

Course link:
  - https://www.udemy.com/course/langchain/learn/lecture/37500842#overview
  - https://www.udemy.com/course/langchain/learn/lecture/37507310#overview
"""

from langchain_core.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain import hub
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    initialize_agent,
    AgentType,
    AgentExecutor,
)

from tools.tools import get_profile_url


def lookup(name: str) -> str:
  llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
  template = """
  Given the full name {name_of_person},
  I want you to get it to me a link to their linkedin profile page.
  Your answer should contain only a URL.
  """
  tools_for_agent = [
      Tool(
          name="Crawl Google for linkedin profile page",
          func=get_profile_url,
          description="useful for when you need to get the Linkedin page URL",
      ),
  ]

  agent = initialize_agent(
      tools=tools_for_agent,
      agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
      verbose=True,
      llm=llm,
  )

  prompt_template = PromptTemplate(
      template=template, input_variables=["name_of_person"])

  name = f'{name} Linkedin'
  linked_profile_url = agent.run(
      prompt_template.format_prompt(name_of_person=name))
  return linked_profile_url
