import orjson
import argparse
from datetime import datetime


class JSONCompiler:
    def __init__(self):
        pass

    def load_json(self, file_path):
        try:
            with open(file_path, "r") as file:
                return orjson.loads(file.read())
        except orjson.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in file {file_path}: {e}")
        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")

    def transform_json(self, data):
        data["compiledAt"] = datetime.now().isoformat()

        def recursive_transform(obj):
            if isinstance(obj, dict):
                return {
                    key.upper(): recursive_transform(value)
                    for key, value in obj.items()
                }
            elif isinstance(obj, list):
                return [recursive_transform(item) for item in obj]
            return obj

        return recursive_transform(data)

    def save_json(self, data, file_path):
        with open(file_path, "wb") as file:
            file.write(orjson.dumps(data, option=orjson.OPT_INDENT_2))
        print(f"Compiled and saved to {file_path}")

    def compile(self, input_file, output_file):
        print(f"Loading JSON from {input_file}")
        data = self.load_json(input_file)

        print("Transforming JSON...")
        transformed_data = self.transform_json(data)

        print(f"Saving compiled JSON to {output_file}")
        self.save_json(transformed_data, output_file)


def main():
    parser = argparse.ArgumentParser(description="JSON Compiler")
    parser.add_argument("input", help="Path to the input JSON file")
    parser.add_argument("output", help="Path to the output JSON file")
    args = parser.parse_args()

    compiler = JSONCompiler()

    try:
        compiler.compile(args.input, args.output)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
