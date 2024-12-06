import json
from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    address: str
    postal_code: str
    pesel: str

    def to_dict(self):
        """Object -> Dictionary"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "postal_code": self.postal_code,
            "pesel": self.pesel,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a class object using dictionary data"""
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            postal_code=data["postal_code"],
            pesel=data["pesel"],
        )

    def save_to_json(self, filename):
        """Save data to JSON."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        """Load data from JSON and create a class"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls.from_dict(data)

# Przykład użycia
if __name__ == "__main__":
    person = Person(
        first_name="Arkadiusz",
        last_name="Kowalczyk",
        address="Ul. Ulicowa 13, Kraków",
        postal_code="30-001",
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

