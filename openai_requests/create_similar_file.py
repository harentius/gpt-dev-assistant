import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join('..')))

class CreateSimilarFile:
    def __init__(self, api_client):
        self.api_client = api_client

    def request(self, file_content, tip):
        messages = [
            {"role": "user", "content":  "I have file: \n" + file_content},
            {"role": "user", "content":  "Create similar file, but for " + tip},
        ]

        res = self.api_client.create_prompt(messages)

        return self._parse_source_code_answer(res)

    def _parse_source_code_answer(self, response):
        try:
            code = re.findall(r'```(.*?)```', response, re.DOTALL)
            if code:
                # Split the code by newlines, remove the first line, and join it back together
                code_lines = code[0].split('\n')[1:]
                code = '\n'.join(code_lines)
                return code.strip()
            else:
                print('Failed to parse the code from the response.')
                return None
        except (KeyError, IndexError):
            print('Failed to parse the response.')
            return None