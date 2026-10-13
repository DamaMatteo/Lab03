

class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno = int(anno)
        self.valore = float(valore)

    def __str__(self):
        return f"[{self.id_strumento}] {self.tipo} della {self.marca} (Acquistato: {self.anno}, Valore: {self.valore}€)"

    def __repr__(self):
        return self.__str__()


class Prestito:
    def __init__(self, id_prestito, data, id_strumento, cognome_allievo):
        self.id_prestito = id_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"Prestito {self.id_prestito}: Strumento {self.id_strumento} a {self.cognome_allievo} (Data: {self.data})"

    def __repr__(self):
        return self.__str__()