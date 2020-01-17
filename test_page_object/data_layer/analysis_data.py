"""
Author:goblinM
Date:2020-01-15
Describe:yaml数据解析
"""
import os

import yaml
# current_path = os.path.abspath(".")
current_path = os.path.dirname(os.path.abspath(__file__))
multiple_yaml_path = os.path.join(current_path, "config.yaml")
single_yaml_path = os.path.join(current_path, "single_config.yaml")


class YamlMethods(object):

    def open_read_file(self, path=single_yaml_path):
        """打开文件"""
        with open(path, 'r', encoding='utf-8') as f:
            file_data = f.read()
            return file_data

    def open_write_file(self, path):
        """写入文件"""
        f = open(path, 'w', encoding='utf-8')
        return f

    def single_yaml_load(self):
        """解析单个yaml文档"""
        file_data = self.open_read_file(single_yaml_path)
        data = yaml.safe_load(file_data)
        print("type:", type(data))
        print(data)
        return data

    def multiple_yaml_load(self):
        """解析多个yaml文档"""
        file_data = self.open_read_file(multiple_yaml_path)
        data_list = yaml.safe_load_all(file_data)
        print("type:", type(data_list))
        for data in data_list:
            print(data)
        return data_list

    def non_standard_yaml_dump(self):
        """dump生成不一定标准的yaml文件 safe_dump 生成标准文档"""
        py_object = {'school': 'zhang',
                     'students': ['a', 'b']}
        file = self.open_write_file(os.path.join(current_path, "output_non_standard_config.yaml"))
        yaml.safe_dump(py_object, file)

    def standard_yaml_dump(self):
        """ruamel 生成标准的yaml文件"""
        from ruamel import yaml
        py_object = {'school': 'zhang',
                     'students': ['a', 'b']
                     }
        file = self.open_write_file(os.path.join(current_path, "output_standard_config.yaml"))
        yaml.dump(py_object, file, Dumper=yaml.RoundTripDumper)


if __name__ == '__main__':
    y = YamlMethods()
    # y.non_standard_yaml_dump()
    # y.standard_yaml_dump()
    y.single_yaml_load()
    # y.multiple_yaml_load()

