import base64

def test_str_func():
    str = u"unicode 编码"
    print(str)
    # base64 UTF-8
    encode_str_by_utf8 = "utf8编码".encode(encoding="UTF-8")
    decode_str_by_utf8 = encode_str_by_utf8.decode("UTF-8")
    print(encode_str_by_utf8, decode_str_by_utf8)

    encode_str_by_base64 = base64.b64encode("base64编码".encode("UTF-8"))
    decode_str_by_base64 = base64.b64decode(encode_str_by_base64.decode())
    print(encode_str_by_base64, decode_str_by_base64)

def test_date_type():
    # python number数据类型包含int  float  bool  complex 4种数据类型
    type_int = 1
    type_float = 0.1
    type_bool = True
    type_complex = complex(1, 1)
    print(type_int, type_float, type_bool, type_complex)
    type_string1 = "abc"
    type_string2 = 'abcd\''
    type_string3 = """
         你好！
            见到你很高兴。
        """
    type_string4 = "abc" + "学习Python字符串" + "通过+拼接"
    print(type_string1, type_string2, type_string3, type_string4)
    type_list = [1, 2, 3, 4]
    type_tuple = ('abc', 'efg', "ddd")
    type_set = {"安徽", "北京"}
    type_dic = {"key1": "value1", "key2": "value2"}
    print(str(type_dic))
    print(type_list, type_tuple, type_set, type_dic)

    if (len(type_list) > 2):
        print(len(type_list))
    elif (len(type_list) > 1):
        print(type_list)
    else:
        print("else")

    for i in range(len(type_list)):
        print(i, type_list[i])

    for k, v in enumerate(type_list):
        print(k, v)

    for k, v in type_dic.items():
        print(k, v)

    a = "abc"
    b = "def"
    c = a + b
    print(a, b, c)

    e = a * 2
    f = e[:2]
    print(e, f, f in e, f not in e, R'\n')

    print("my name is %s and age is %d!" % ('zhangsan', 20))

if __name__ == "__main__" :
    test_date_type()
    test_str_func()
