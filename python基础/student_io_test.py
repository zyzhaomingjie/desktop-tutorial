import unittest
import csv
import json

def convert_file_format(input_file_path: str, output_file_path: str,
                        input_format: str = 'csv', output_format: str = 'json'):
    csvfile = open(input_file_path,'r', encoding='utf-8')
    jsonfile = open(output_file_path, 'w',encoding='utf-8')
    # 指定列名
    fieldnames = ("name", "age", "gender", "class", "score")
 
    reader = csv.DictReader( csvfile, fieldnames)
    # 指定ensure_ascii=False 为了不让中文显示为ascii字符码
    out = json.dumps( [ row for row in reader ] ,ensure_ascii=False)
 
    jsonfile.write(out)


class StudentIOTest(unittest.TestCase):
    def test_convert_file_format(self):
        convert_file_format('./student.csv', './student.json', 'csv', 'json')

        with open('./student.json', 'r', encoding='utf8') as f:
            students = json.load(f)
        
        self.assertDictEqual(students[1], {
            'name': '张三', 'age': 18, 'gender': '男', 'class': '高三三班', 'score': 98
        })##匹配失败

        self.assertDictEqual(students[1], {
            'name': '张三', 'age': '18', 'gender': '男', 'class': '高三三班', 'score': '98'
        })##匹配成功


if __name__ == '__main__':
    unittest.main()
