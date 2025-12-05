def has_duplicates(lst):
    return len(lst) != len(set(lst))
test_cases = [
    [1, 2, 3, 4],       
    [1, 2, 2, 3],       
    ["a", "b", "a"],    
    []                  
]
for case in test_cases:
    result = has_duplicates(case)
    print("列表 {0} 有重复元素：{1}".format(case,result))
