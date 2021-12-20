import requests
import json
import re
from bs4 import BeautifulSoup
ta_lib = requests.get('https://mrjbq7.github.io/ta-lib/func_groups/pattern_recognition.html')

# print(ta_lib.text)

soup = BeautifulSoup(ta_lib.text, 'html.parser')

body = soup.find('body')

patterns_elements = body.find_all('h3')

x = {}

for pattern_element in patterns_elements:
    pattern_index = patterns_elements.index(pattern_element)
    code_lines = body.find_all('pre')[pattern_index]
    split_text = re.split('-'[0], pattern_element.text)
    function_name_replace = split_text[0].lower()
    
    code_lines_text = code_lines.text.replace('\n', '').replace('integer', function_name_replace)
    print(code_lines_text.lower())

    splitter = re.search('-' , pattern_element.text)
    x[pattern_index] = {
        "pattern_name":split_text[1],
        "pattern_function_name":split_text[0],
        "pattern_function_code":code_lines_text
    }
