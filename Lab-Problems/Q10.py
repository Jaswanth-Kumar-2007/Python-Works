import re

def is_valid_vehicle_number(number):
    s = number.split("-")
    if s[0][0].isupper() and s[0][1].isupper() and len(s[0]) == 2:
        try:
            int(s[1])
            if len(str((s[1]))) == 2:
                if s[2][0].isupper() and s[2][1].isupper() and len(s[2]) == 2:
                    try:
                        int(s[3])
                        if len(str(s[3])) == 4:
                            return True
                        else:
                            return False
                    except:
                        return False
                else:
                    return False
            else:
                return False
        except:
            return False
    else:
        return False

print(is_valid_vehicle_number('AB-12-CD-1234'))
