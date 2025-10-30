def validate_and_strip_pkcs7_padding(plaintext):
    """
    验证并去除PKCS#7填充

    参数:
        plaintext: 带填充的明文字符串或字节串

    返回:
        去除填充后的数据

    异常:
        ValueError: 当填充无效时抛出
    """
    if len(plaintext) == 0:
        raise ValueError("数据长度不能为0")

    # 确保处理字节数据
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('latin-1')

    # 获取最后一个字节的值（填充长度）
    pad_length = plaintext[-1]

    # 检查填充长度是否有效
    if pad_length < 1 or pad_length > len(plaintext):
        raise ValueError("无效的填充长度")

    # 检查所有填充字节是否正确
    expected_padding = bytes([pad_length]) * pad_length
    actual_padding = plaintext[-pad_length:]

    if actual_padding != expected_padding:
        raise ValueError("无效的PKCS#7填充")

    # 返回去除填充的数据
    return plaintext[:-pad_length]


# 测试示例
if __name__ == "__main__":
    # 有效填充的测试用例
    test_cases_valid = [
        "ICE ICE BABY\x04\x04\x04\x04",
        b"TEST\x03\x03\x03",
        b"A" * 8 + b"\x08" * 8,  # 完整块的填充
    ]

    # 无效填充的测试用例
    test_cases_invalid = [
        "ICE ICE BABY\x05\x05\x05\x05",
        "ICE ICE BABY\x01\x02\x03\x04",
        b"WRONG\x00",  # 零填充无效
        b"SHORT",  # 无填充字节
        b"\x10" * 17,  # 填充长度超过数据长度
    ]

    print("测试有效填充:")
    for i, test_case in enumerate(test_cases_valid):
        try:
            result = validate_and_strip_pkcs7_padding(test_case)
            print(f"  用例 {i + 1}: 成功 -> {result}")
        except ValueError as e:
            print(f"  用例 {i + 1}: 失败 -> {e}")

    print("\n测试无效填充:")
    for i, test_case in enumerate(test_cases_invalid):
        try:
            result = validate_and_strip_pkcs7_padding(test_case)
            print(f"  用例 {i + 1}: 意外成功 -> {result}")
        except ValueError as e:
            print(f"  用例 {i + 1}: 正确捕获异常 -> {e}")