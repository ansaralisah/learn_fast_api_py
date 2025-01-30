import re


class AppConstant:
    def check_password_strength(password):
        length_criteria = len(password) >= 8
        digit_criteria = bool(re.search(r"\d", password))
        lowercase_criteria = bool(re.search(r"[a-z]", password))
        uppercase_criteria = bool(re.search(r"[A-Z]", password))
        special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

        score = sum([length_criteria, digit_criteria, lowercase_criteria, uppercase_criteria, special_char_criteria])

        if score < 3:
            return "Weak Password"
        elif score == 3 or score == 4:
            return "Normal Password"
        else: 
            return "Strong Password"

        
    def getErrorModel(error):
        return {
            "status": "error",
            "data":"error",
            "message": str(error),
        }
    
    def getSuccessModel(data):
        return {
            "status": "success",
            "data": data,
            "message": 'success',
        }	
    
  

