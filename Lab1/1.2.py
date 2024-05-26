#交换ab的逻辑如下,a变temp，b变a，temp变b
def FormulaTransfer(str):
    str=str.replace('∨', 'temp')
    str=str.replace('∧', '∨')
    str=str.replace('temp', '∧')
    str=str.replace('1', 'temp')
    str=str.replace('0', '1')
    str =str.replace('temp', '0')
    return str

str = input("输入合式公式：")
print("该公式的对偶式为：",FormulaTransfer(str))
