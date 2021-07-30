def is_anagram(test, original):
    test_list = list(test).lower().sort()
    return test_list

print(is_anagram("Buckethead", "DeathCubeK"))