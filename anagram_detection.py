def is_anagram(test, original):
    test_list = sorted(list(test.lower()))
    original_list = sorted(list(original.lower()))
    return test_list == original_list
    
print(is_anagram("Buckethead", "DeathCubeK"))