import winreg
def deleteSubkey(key0, key1, key2=""):
    
    if key2=="":
        currentkey = key1
    else:
        currentkey = key1+ "\\" +key2

    open_key = winreg.OpenKey(key0, currentkey ,0,winreg.KEY_ALL_ACCESS)
    infokey = winreg.QueryInfoKey(open_key)
    for x in range(0, infokey[0]):
        
        subkey = winreg.EnumKey(open_key, 0)
        try:
            winreg.DeleteKey(open_key, subkey)
            print ("Removed %s\\%s " % ( currentkey, subkey))
        except:
            deleteSubkey( key0, currentkey, subkey )
            # no extra delete here since each call 
            #to deleteSubkey will try to delete itself when its empty.

    winreg.DeleteKey(open_key,"")
    open_key.Close()
    print ("Removed %s" % (currentkey))
    return

deleteSubkey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\Application_w_Bad_intention")