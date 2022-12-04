import winreg
access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE) 
access_key = winreg.OpenKey(access_registry,r"SOFTWARE\Microsoft\Windows\CurrentVersion")
#create a new key 
new_key = winreg.CreateKey(access_key,"Application_w_Bad_intention")#this like a folder where the new_key is stored
winreg.SetValueEx(new_key, "Value-1",0,winreg.REG_SZ,"[*] Value-1 initialized") #Value-1 is the name of the value 
if new_key:
    winreg.CloseKey(new_key)
#Adds new key to the given registry
