import json

class Person:
    def __init__(self, first_name, last_name, address, postal_code, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.postal_code = postal_code
        self.pesel = pesel

    def to_dict(self):
        """Konwertuje obiekt na słownik."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "postal_code": self.postal_code,
            "pesel": self.pesel,
        }

    @classmethod
    def from_dict(cls, data):
        """Tworzy obiekt klasy na podstawie słownika."""
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            postal_code=data["postal_code"],
            pesel=data["pesel"],
        )

    def save_to_json(self, filename):
        """Zapisuje dane obiektu do pliku JSON."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        """Wczytuje dane z pliku JSON i tworzy obiekt klasy."""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls.from_dict(data)

# Przykład użycia
if __name__ == "__main__":
    # Tworzenie obiektu
    person = Person(
        first_name="Jan",
        last_name="Kowalski",
        address="Ul. Kwiatowa 12, Warszawa",
        postal_code="00-001",
        pesel="12345678901"
    )

    # Zapis do pliku JSON
    person.save_to_json("person.json")

    # Wczytanie z pliku JSON
    loaded_person = Person.load_from_json("person.json")

    # Wyświetlenie wczytanych danych
    print("Imię:", loaded_person.first_name)
    print("Nazwisko:", loaded_person.last_name)
    print("Adres:", loaded_person.address)
    print("Kod pocztowy:", loaded_person.postal_code)
    print("PESEL:", loaded_person.pesel)
