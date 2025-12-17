from datetime import datetime, timedelta

class Device:
    def __init__(self, device_id, device_type, owner, firmware_version='1.0.0'):
        self.__device_id = device_id
        self.__device_type = device_type
        self.__firmware_version = firmware_version
        self.__compliance_status = 'unknown'
        self.__owner = owner
        self.__last_security_scan = None
        self.__is_active = True
        self.__access_log = []
    
    def authorise_access(self, user):
        if not self.__is_active:
            self.__log_access(user.get_username(), 'Denied - Device inactive')
            return False
        
        if self.__compliance_status != 'compliant':
            if not user.check_privileges('admin'):
                self.__log_access(user.get_username(), 'Denied - Non-compliant device')
                return False
        
        if self.__owner != user.get_username() and not user.check_privileges('admin'):
            self.__log_access(user.get_username(), 'Denied - Not owner')
            return False
        
        self.__log_access(user.get_username(), 'Access granted')
        return True
    
    def run_security_scan(self):
        self.__last_security_scan = datetime.now()
        self.__compliance_status = 'compliant'
        self.__log_access('SYSTEM', 'Security scan completed')
    
    def check_compliance(self):
        if self.__last_security_scan is None:
            self.__compliance_status = 'unknown'
            return False
        
        days_since_scan = (datetime.now() - self.__last_security_scan).days
        if days_since_scan > 30:
            self.__compliance_status = 'non-compliant'
            return False
        
        return self.__compliance_status == 'compliant'
    
    def update_firmware(self, version, user):
        if not user.check_privileges('admin'):
            return False
        
        self.__firmware_version = version
        self.__log_access(user.get_username(), f'Firmware updated to {version}')
        return True
    
    def quarantine(self, user):
        if not user.check_privileges('admin'):
            return False
        
        self.__is_active = False
        self.__log_access(user.get_username(), 'Device quarantined')
        return True
    
    def __log_access(self, username, action):
        self.__access_log.append(f"{datetime.now()}: {username} - {action}")
    
    def get_device_info(self):
        return {
            'device_id': self.__device_id,
            'device_type': self.__device_type,
            'firmware_version': self.__firmware_version,
            'compliance_status': self.__compliance_status,
            'owner': self.__owner,
            'is_active': self.__is_active
        }

class DeviceManager:
    def __init__(self):
        self.__devices = {}
    
    def add_device(self, device):
        device_info = device.get_device_info()
        self.__devices[device_info['device_id']] = device
    
    def remove_device(self, device_id, user):
        if not user.check_privileges('admin'):
            return False
        
        if device_id in self.__devices:
            del self.__devices[device_id]
            return True
        return False
    
    def generate_security_report(self, user):
        if not user.check_privileges('admin'):
            return None
        
        report = []
        for device_id, device in self.__devices.items():
            info = device.get_device_info()
            device.check_compliance()
            report.append(info)
        
        return report
