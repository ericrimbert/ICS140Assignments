# 1.4.1 - Basic syntax errors

# I guess we are just fixing syntax errors
"""
    ---Old syntax that was wrong---
    print('Predictions are hard.")  # Quotes do not match
    print(Especially about the future.)  # Missing quotes all together
    user_num = 5  # this is fine
    print('user_num is:' user_num)  # There is no comma after the quotes, so user_num is not expected
"""

# Fixed syntax errors
print('Predictions are hard.')
print('Especially about the future.')
user_num = 5
print('user_num is:', user_num)
