class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_index = 0
        typed_index = 0
        name_len = len(name)
        typed_len = len(typed)
        if typed == name:
            return True

        if typed_len < name_len:
            return False

        while name_index <= name_len - 1:
            if name[name_index] == typed[typed_index]:
                name_index += 1
                typed_index += 1
            else:
                typed_index += 1

            if typed_index == typed_len and name_index != name_len:
                return False
        return True