from operator import attrgetter
from strumento import Strumento, Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []
        self.contatore_prestiti = 1

    def carica_file_strumenti(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for riga in file:
                    riga = riga.strip()
                    if riga != "":  # Salta eventuali righe vuote
                        dati = riga.split(",")
                        id_strum = dati[0]
                        tipo = dati[1]
                        marca = dati[2]
                        anno = dati[3]
                        valore = dati[4]

                        # Usa la classe importata dall'altro file
                        nuovo_strumento = Strumento(id_strum, tipo, marca, anno, valore)
                        self.strumenti.append(nuovo_strumento)
        except FileNotFoundError:
            raise FileNotFoundError(f"Errore: Il file {file_path} non è stato trovato.")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        max_id = 0
        for s in self.strumenti:
            numero_id = int(s.id_strumento[1:])
            if numero_id > max_id:
                max_id = numero_id

        nuovo_id = f"S{max_id + 1}"
        nuovo_strumento = Strumento(nuovo_id, tipo, marca, anno_acquisto, valore)

        self.strumenti.append(nuovo_strumento)
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        return sorted(self.strumenti, key=attrgetter("marca"))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        strumento_esiste = False
        for s in self.strumenti:
            if s.id_strumento == id_strumento:
                strumento_esiste = True
                break

        if not strumento_esiste:
            raise Exception("Errore: lo strumento richiesto non è presente nel sistema.")

        for p in self.prestiti:
            if p.id_strumento == id_strumento:
                raise Exception("Errore: lo strumento è già attualmente in prestito.")

        id_prestito = f"P{self.contatore_prestiti}"
        self.contatore_prestiti += 1

        nuovo_p = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(nuovo_p)
        return nuovo_p

    def termina_prestito(self, id_prestito):
        prestito_da_rimuovere = None
        for p in self.prestiti:
            if p.id_prestito == id_prestito:
                prestito_da_rimuovere = p
                break

        if prestito_da_rimuovere is None:
            raise Exception("Errore: Nessun prestito trovato con questo codice.")
        else:
            self.prestiti.remove(prestito_da_rimuovere)