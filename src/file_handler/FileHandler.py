from typing import List

class FileHandler:

    @staticmethod
    def open_input_file(input_file_path: str) -> List[str]:
        with open(input_file_path, mode='r', encoding='utf-8') as input_file:
            input_data_raw = input_file.readlines()
            input_data = []
            for data in input_data_raw:
                data_treated = data.strip()
                if(data_treated != ''):
                    input_data.append(data_treated)
            return input_data

    @staticmethod
    def save_output_file(output_data: str) -> None:
        with open(output_data, mode='w', encoding='utf-8'):
            ...
