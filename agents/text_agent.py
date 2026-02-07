from langchain_openai import ChatOpenAI
import os

class TextAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",  # cheaper + fast, good for docs
            temperature=0
        )

    def analyze(self, text: str):
        prompt = f"""
        You are a document understanding agent.
        Extract structured information from the following content:

        {text}
        """
        return self.llm.invoke(prompt).content
