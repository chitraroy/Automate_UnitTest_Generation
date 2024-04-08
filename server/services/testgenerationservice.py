from openai import OpenAI
import environ

env = environ.Env()
environ.Env.read_env()
class TestGenerationService:
    def __init__(self):
        self.client = OpenAI(api_key=env('OPENAI_API_KEY'))
    
    def generate_test(self, code_block)-> dict:
        # placeholder for logic to generate test using LLM
        # prompt_for_tests = f"""Write comprehensive unit tests in Python for the following
        #   function:\n{code_block}"""
        messages_code = [
            {'role': 'system', 'content': 'Write comprehensive unit tests in Python for the following function:'},
            {'role': 'user', 'content': code_block}
        ]
        generated_test = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages_code,
        )
        
        # placeholder for logic to get explanation from LLM
        # prompt_for_explanation = f"""Explain the following Python function and its unit tests
        #   in simple terms:\nFunction:\n{code_block}\nGenerated Unit Tests:\n
        #   {generated_test.choices[0].text}"""
        message_explanation = [
            {'role': 'system', 'content': 'Explain the following Python function and its unit tests in simple terms:'},
            {'role': 'user', 'content': code_block},
            {'role': 'user', 'content': generated_test.choices[0].message.content}
        ]
        explanation = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message_explanation
        )

        return {'test': generated_test.choices[0].message.content,
                 'explanation': explanation.choices[0].message.content}