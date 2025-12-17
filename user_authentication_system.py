from datetime import datetime

class User:
    def __init__(self, username, password, privilege_level='standard'):
        self.__username = username
        self.__password_hash = self.__hash_password(password)
        self.__privilege_level = privilege_level
        self.__login_attempts = 0
        self.__account_status = 'active'
        self.__activity_log = []
    
    def __hash_password(self, password):
        return f"hashed_{password}"
    
    def authenticate(self, password):
        if self.__account_status == 'locked':
            self.__log_activity('Login attempt on locked account')
            return False
        
        if self.__hash_password(password) == self.__password_hash:
            self.__login_attempts = 0
            self.__log_activity('Successful login')
            return True
        else:
            self.__login_attempts += 1
            self.__log_activity(f'Failed login attempt {self.__login_attempts}')
            if self.__login_attempts >= 3:
                self.lock_account()
            return False
    
    def check_privileges(self, required_level):
        privilege_hierarchy = {'guest': 0, 'standard': 1, 'admin': 2}
        return privilege_hierarchy.get(self.__privilege_level, 0) >= privilege_hierarchy.get(required_level, 0)
    
    def lock_account(self):
        self.__account_status = 'locked'
        self.__log_activity('Account locked due to failed login attempts')
    
    def reset_login_attempts(self, admin_password):
        if self.__hash_password(admin_password) == 'hashed_admin_secret':
            self.__account_status = 'active'
            self.__login_attempts = 0
            self.__log_activity('Account unlocked by admin')
            return True
        return False
    
    def __log_activity(self, message):
        self.__activity_log.append(f"{datetime.now()}: {message}")
    
    def get_safe_info(self):
        return {
            'username': self.__username,
            'privilege_level': self.__privilege_level,
            'account_status': self.__account_status
        }
    
    def get_username(self):
        return self.__username
    
    def get_privilege_level(self):
        return self.__privilege_level
