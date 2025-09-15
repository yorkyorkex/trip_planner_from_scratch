from crewai import Agent
from textwrap import dedent
from openai import OpenAI
#import ollama
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

# 創建工具實例
search_tool = SearchTools.search_internet
calculator_tools = CalculatorTools()
calculator_tool = calculator_tools.calculate



"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee
  you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal.
- Define which experts the captain needs to communicate with and delegate tasks to.
  Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert
- Local Tour Guide

Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        pass  # CrewAI 會自動使用環境變數中的 OPENAI_API_KEY

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""An experienced travel agent with a passion for creating personalized itineraries. Has traveled to over 50 countries and has a deep understanding of various cultures and travel logistics."""),
            goal=dedent(f"""Create a comprehensive 7-day travel itinerary for a client, including budget, packing suggestions, and safety tips."""),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""A knowledgeable travel consultant specializing in selecting the best cities for various types of travelers. Has a knack for understanding client preferences and matching them with ideal destinations."""),
            goal=dedent(f"""Identify the top 3 cities for a client's 7-day trip based on their interests, budget, weather, season, and travel style."""),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""A friendly and knowledgeable local guide with extensive experience in showing travelers the hidden gems of their city. Passionate about sharing local culture, history, and cuisine."""),
            goal=dedent(f"""Create a detailed daily itinerary for the client's 7-day trip, including must-see attractions, local dining options, and unique experiences."""),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
        )
