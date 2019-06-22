from Crypto.Hash import SHA256


class Sha256:
    def __init__(self, senha):
        self.hash = self.criptografar(senha)

    def criptografar(self, senha):
        sha = SHA256.new()
        sha.update(bytes(senha, encoding='utf-8'))

        return sha.hexdigest()  
