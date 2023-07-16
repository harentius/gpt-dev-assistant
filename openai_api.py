import openai
import re

class OpenAIAPI:
    def __init__(self, api_key, model="gpt-4"):
        self.model = model
        openai.api_key = api_key

    def request(self, messages):
        messages.insert(0, {"role": "system", "content": "You are a helpful assistant."})

        try:
            response = openai.ChatCompletion.create(model=self.model, messages=messages)

            return response['choices'][0]['message']['content']


        except openai.error.InvalidRequestError as e:
            if self.model == "gpt-4":
                print(f"GPT-4 model failed with error: {e}. Falling back to gpt-3.5-turbo.")
                self.model = "gpt-3.5-turbo"
                return self.request(messages)
            else:
                print(f"Error occurred: {e}")
                return None

    def request_only_source_code(self, messages):
        response = self.request(messages)

        return self._parse_source_code_from_answer(response)

    def _parse_source_code_from_answer(self, response):
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
