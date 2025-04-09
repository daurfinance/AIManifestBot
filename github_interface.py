import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

class GitHubInterface:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("GITHUB_TOKEN is not set in the environment variables.")
        self.repo_owner = os.getenv("REPO_OWNER")
        self.repo_name = os.getenv("REPO_NAME")
        if not self.repo_owner or not self.repo_name:
            raise ValueError("REPO_OWNER or REPO_NAME is not set in the environment variables.")
        self.github = Github(self.token)
        self.repo = self.github.get_repo(f"{self.repo_owner}/{self.repo_name}")

    def commit_changes(self, file_path, content, message):
        try:
            file = self.repo.get_contents(file_path)
            self.repo.update_file(file.path, message, content, file.sha)
        except Exception:
            self.repo.create_file(file_path, message, content)

    def get_logs(self):
        # Заглушка для логов
        return "Логи недоступны"

    def get_summary(self):
        # Заглушка для сводки
        return "Сводка недоступна"