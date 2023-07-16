import argparse
import os

from file_manager import FileManager
from openai_requests.create_similar_file import CreateSimilarFile
from openai_api import OpenAIAPI

def main():
    api_key = os.getenv('OPENAI_API_KEY')

    if api_key is None:
        print("The environment variable OPENAI_API_KEY is not set.")

    parser = argparse.ArgumentParser(description='Perform file operations.')
    parser.add_argument('action', type=str, help='The action to perform. Options are "similar" or "tests".')
    parser.add_argument('filepath', type=str, help='The path to the file.')
    parser.add_argument('description', type=str, nargs='?', default='', help='Extra clarification (optional)')

    args = parser.parse_args()

    fm = FileManager()
    openai_api = OpenAIAPI(api_key)

    if args.action.lower() == 'similar' or args.action.lower() == 's':
        create_similar_file = CreateSimilarFile(openai_api)

        input_file_path = args.filepath
        input_file_content = fm.read_file(input_file_path)
        name = args.description
        output_file_content = create_similar_file.request(input_file_content, name)

        dir_name = os.path.dirname(input_file_path)
        output_file_path = os.path.join(dir_name, name)

        fm.write_file(output_file_path, output_file_content)

    elif args.action.lower() == 'tests' or args.action.lower() == 't':
        filecontent = fm.read_file(args.filepath)

    else:
        print(f'Error: Unknown action "{args.action}". Options are "similar" or "tests".')

if __name__ == "__main__":
    main()
