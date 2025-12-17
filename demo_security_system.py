from datetime import datetime
from user_authentication_system import User
from iot_device_management import Device, DeviceManager

def main():
    print("=" * 60)
    print("SECURE USER AUTHENTICATION & IoT DEVICE MANAGEMENT DEMO")
    print("=" * 60)
    
    admin = User('admin', 'admin123', 'admin')
    standard_user = User('john_doe', 'password123', 'standard')
    
    print("\n--- User Authentication Tests ---")
    print(f"Admin login (correct password): {admin.authenticate('admin123')}")
    print(f"Standard user login (wrong password): {standard_user.authenticate('wrong')}")
    print(f"Standard user login (wrong password): {standard_user.authenticate('wrong')}")
    print(f"Standard user login (wrong password): {standard_user.authenticate('wrong')}")
    print(f"Account status: {standard_user.get_safe_info()['account_status']}")
    
    print("\n--- IoT Device Management Tests ---")
    manager = DeviceManager()
    
    device1 = Device('DEV001', 'SmartCamera', 'john_doe')
    device2 = Device('DEV002', 'SmartLock', 'admin')
    
    manager.add_device(device1)
    manager.add_device(device2)
    
    print(f"Standard user access to own device: {device1.authorise_access(standard_user)}")
    print(f"Standard user access to admin's device: {device2.authorise_access(standard_user)}")
    print(f"Admin access to any device: {device2.authorise_access(admin)}")
    
    device1.run_security_scan()
    print(f"Device compliance after scan: {device1.check_compliance()}")
    
    print("\n--- Security Report ---")
    report = manager.generate_security_report(admin)
    if report:
        for device_info in report:
            print(f"Device: {device_info['device_id']}")
            print(f"  Type: {device_info['device_type']}")
            print(f"  Owner: {device_info['owner']}")
            print(f"  Compliance: {device_info['compliance_status']}")
            print(f"  Active: {device_info['is_active']}")
            print()
    
    print("=" * 60)

if __name__ == "__main__":
    main()
