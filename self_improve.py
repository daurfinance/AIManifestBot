from gpt_engine import GPT
from github_interface import GitHubInterface

def self_improve():
    gpt = GPT()
    github = GitHubInterface()
    prompt = "Как можно улучшить текущий проект?"
    suggestion = gpt.generate_code(prompt)
    github.commit_changes(
        file_path="self_improvement.txt",
        content=suggestion,
        message="Auto-generated self-improvement suggestion"
    )