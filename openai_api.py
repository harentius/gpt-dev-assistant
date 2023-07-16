import openai

class OpenAIAPI:
    def __init__(self, api_key, model="gpt-4"):
        self.model = model
        openai.api_key = api_key

    def create_prompt(self, messages):
        messages.insert(0, {"role": "system", "content": "You are a helpful assistant."})

        try:
            response = openai.ChatCompletion.create(model=self.model, messages=messages)

            return response['choices'][0]['message']['content']


        except openai.error.InvalidRequestError as e:
            if self.model == "gpt-4":
                print(f"GPT-4 model failed with error: {e}. Falling back to gpt-3.5-turbo.")
                self.model = "gpt-3.5-turbo"
                return self.create_prompt(messages)
            else:
                print(f"Error occurred: {e}")
                return None
