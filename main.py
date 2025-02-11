def loger():
    print(error_msg)

error_msg=None

def getinfo():
    print("lunching GUI...")
    import gui


def mains():
    #threading.Thread(target=getinfo, daemon=True).start()
    getinfo()
