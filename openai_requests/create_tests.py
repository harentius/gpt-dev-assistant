import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))

class CreateTests:
    def __init__(self, api_client):
        self.api_client = api_client

    def request(self, file_content):
        messages = [
            {"role": "user", "content":  "I have file: \n" + file_content},
            {"role": "user", "content":  "Write tests for it. Use only PHPUnit mocks, no mockery. Cover as many scenarios as it is meaningful"},
        ]

        return self.api_client.request_only_source_code(messages)
