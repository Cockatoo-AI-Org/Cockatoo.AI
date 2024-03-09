## Langchain - Leverage agent to query information from Google

This section demonstrates how LangChain utilizes agents to query Google for
information it lacks and then extract the relevant parts to answer the question.
To try the sample code below, you'll need to complete some preparation steps.

### Prerequisite

* Please go to register or login https://serpapi.com/dashboard to retrieve API
  key and save it as environment variable `SERPAPI_API_KEY` in file `.env`
* Pleae go to register or login https://platform.openai.com/api-keys to retrieve
  API key and save it as environment variable `OPENAI_API_KEY` in file `.env`
* Create a virtual python runtime environment and install necessary packages:

```shell
$ virtualenv env
$ source env/bin/active
(env) $ pip install -r requirements.txt
...
```


### Sample code
Please follow below instructions to query the Linkedin URL of people with
searching string as "Google Test Engineer Lee John":
```python
>>> from agents.linkedin_lookup_agent import lookup
>>> lookup('Google Test Engineer Lee John')
...
> Entering new AgentExecutor chain...
I should use the tool to crawl Google for the Linkedin profile page of Google Test Engineer Lee John.
Action: Crawl Google for linkedin profile page
Action Input: Google Test Engineer Lee John LinkedinSaving search result into search_5066441651125638471.txt...

Observation: https://tw.linkedin.com/in/lee-john-81601a7a
Thought:I now know the final answer
Final Answer: https://tw.linkedin.com/in/lee-john-81601a7a

> Finished chain.
'https://tw.linkedin.com/in/lee-john-81601a7a'
```

The final result is `https://tw.linkedin.com/in/lee-john-81601a7a` which is
correct as my Linkedin URL.
