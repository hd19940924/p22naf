import json
import os
import unittest
import ddt
#from Base import HTMLTestRunner_PY3
import Base.HTMLTestRunner_PY3 as HTMLTestRunner_py3
from Util.get_condition import get_data
from Util.get_result import handle_result, get_result_json, handle_result_json
from Util.get_header import get_header
base_path = os.getcwd()  #当前路径
path = os.path.abspath(os.path.dirname(os.getcwd()))  #上级路径
from Util.get_excel import excel_data
from Base.base_request import base_request

data =excel_data.get_excel_data()
print(data)

@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):
    @ddt.data(*data)
    def test_main_case(self, data):
        header = None
        #data = excel_data.get_rows_value(i + 2)   #使用ddt，就不需要获取这个data了
        is_run = data[2]  # 是否执行
        case_id = data[0]   #获取case_id编辑
        line_num = excel_data.get_row_number(case_id) #通过case_id 获取行号；结果回写的时候就需要这个
        if is_run == 'yes':
            data1 = data[7]
            # data1 = json.loads(data[7])  #将data数据转成dict格式
            is_depend = data[3]
            # 获取依赖数据
            try:
                if is_depend:  # 如果有依赖数据
                    depend_key = data[4]  # 依赖的值
                    depend_data = get_data(is_depend)  # 依赖数据：将前置条件赋值给依赖数据
                    depend_data = depend_data[0]  # 最终依赖的数据
                    # data1[depend_key] = depend_data    #这个主要目前也是提取，但是目前报错，待处理。
                method = data[6]
                url = data[5]
                is_header = data[9]
                excepect_method = data[10]
                excepect_result = data[11]
                condition = data[3]
                if condition:
                    pass
                if is_header == 'yes':
                    header = get_header()
                res = base_request.run_main(method, url, data1, header).json()
                code = res['code']
                message = res['msg']
                if excepect_method == "mec":  # mec表示:用例里面的预期结果方式为message+code
                    config_message = handle_result(url, code)
                    try:
                        self.assertEqual(message, config_message)
                        excel_data.write_excel_data(line_num, 13, "通过")
                        excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        excel_data.write_excel_data(line_num, 13, "失败")
                        excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))
                        raise e


                    # if message == config_message:
                    #     excel_data.write_excel_data(line_num, 13, "通过")
                    #     excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))
                    #
                    # else:
                    #     excel_data.write_excel_data(line_num, 13, "失败")
                    #     excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))

                if excepect_method == "code":  # code表示：用例里面的预期结果方式为code
                    try:
                        self.assertEqual(excepect_result, code)
                        excel_data.write_excel_data(line_num, 13, "通过")
                        excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        excel_data.write_excel_data(line_num, 13, "失败")
                        excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))
                        raise e



                if excepect_method == 'json':  # json表示：用例里面的预期结果方式为json； 主要是用来做对比，将期望的result.json里面的与最终请求返回的数据进行对比
                    if code == 0:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    excepect_result = get_result_json(url, status_str)
                    result = handle_result_json(res, excepect_result)
                    try:
                        self.assertTrue(result)
                        excel_data.write_excel_data(line_num, 13, "通过")
                        excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        excel_data.write_excel_data(line_num, 13, "失败")
                        excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))
                        raise e

                    # if result:
                    #     excel_data.write_excel_data(line_num, 13, "通过")
                    #     excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))
                    #
                    # else:
                    #     excel_data.write_excel_data(line_num, 13, "失败")
                    #     excel_data.write_excel_data(line_num, 14, json.dumps(res, ensure_ascii=False))

            except Exception as e:
                excel_data.write_excel_data(line_num, 13, "失败")
                raise e

if __name__ == '__main__':
    case_path = path +"/hd_api/Run"
    report_path = path + "/hd_api/Report/report1.html"
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run_case_*.py")
    with open(report_path, "w",encoding='utf-8') as f:
        runner = HTMLTestRunner_py3.HTMLTestRunner(stream=f, title="hd", description="YIQ测试报告")
        runner.run(discover)
        f.close()
