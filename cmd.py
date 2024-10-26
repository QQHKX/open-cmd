import winreg

def enable_cmd():
    try:
        # 注册表路径
        reg_path = r"Software\Policies\Microsoft\Windows\System"
        
        # 打开注册表键
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE) as registry_key:
            try:
                # 删除 DisableCMD 键值
                winreg.DeleteValue(registry_key, "DisableCMD")
                print("CMD 已成功启用。")
            except FileNotFoundError:
                print("DisableCMD 键不存在，CMD 已启用。")
    
    except PermissionError:
        print("权限不足，请以管理员身份运行该脚本。")
    
    except Exception as e:
        print(f"发生错误: {e}")

# 执行函数
enable_cmd()

input("按任意键退出...")
