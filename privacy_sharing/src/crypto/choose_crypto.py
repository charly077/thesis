def Crypto(name, conf, metadata=None):
    if (name == 'pbkdf2'):
        from crypto.pbkdf2 import Pbkdf2
        return Pbkdf2(conf, metadata)