# search_tools.py
from crewai_tools import SerperDevTool


class SearchTools:
    # 使用 CrewAI 內建的 SerperDevTool
    search_internet = SerperDevTool()
