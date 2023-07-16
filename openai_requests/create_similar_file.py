import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))

class CreateSimilarFile:
    def __init__(self, api_client):
        self.api_client = api_client

    def request(self, file_content, tip):
        messages = [
            {"role": "user", "content":  "I have file: \n" + file_content},
            {"role": "user", "content":  "Create similar file, but for " + tip},
        ]

        return self.api_client.request_only_source_code(messages)
