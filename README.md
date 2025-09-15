scoop install pipx
pipx ensurepath
scoop update pipx
pipx install poetry
poetry install --no-root # 1. 建立虛擬環境（如果不存在）# 2. 安裝依賴到該環境
poetry env list
poetry env activate # 啟動虛擬環境 (Poetry 2.0+)
poetry run python your_script.py # 在虛擬環境中執行 Python

## agents.py

This file contains the definition of custom agents.
To create a Agent, you need to define the following:

1. Role: The role of the agent.
2. Backstory: The backstory of the agent.
3. Goal: The goal of the agent.
4. Tools: The tools that the agent has access to (optional).
5. Allow Delegation: Whether the agent can delegate tasks to other agents(optional).

   [More Details about Agent](https://docs.crewai.com/concepts/agents).

## task.py

This file contains the definition of custom tasks.
To Create a task, you need to define the following :

1. description: A string that describes the task.
2. agent: An agent object that will be assigned to the task.
3. expected_output: The expected output of the task.

   [More Details about Task](https://docs.crewai.com/concepts/tasks).

## crew (main.py)

This is the main file that you will use to run your custom crew.
To create a Crew , you need to define Agent ,Task and following Parameters:

1. Agent: List of agents that you want to include in the crew.
2. Task: List of tasks that you want to include in the crew.
3. verbose: If True, print the output of each task.(default is False).
4. debug: If True, print the debug logs.(default is False).

   [More Details about Crew](https://docs.crewai.com/concepts/crew).
