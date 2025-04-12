from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS desteği

app = Flask(__name__)
CORS(app)  # Tüm domainlere istek izni verir

@app.route("/produktfinder", methods=["POST"])
def produktfinder():
    data = request.json
    kategorie = data.get("kategorie")

    def frage_sonnenschutz(antwort):
        if antwort == "einflügelig":
            return "Ihre Empfehlung: Produkt 12"
        elif antwort == "zweiflügelig":
            return "Ihre Empfehlung: Produkt 10"

    def frage_dachfenster(verstaerkung, fluegel):
        if verstaerkung == "mit verstärkung":
            return "Ihre Empfehlung: Produkt 11"
        elif verstaerkung == "ohne verstärkung":
            if fluegel == "einflügelig":
                return "Ihre Empfehlung: Produkt 6"
            elif fluegel == "zweiflügelig":
                return "Ihre Empfehlung: Produkt 5"

    def frage_terrassentuer(fluegel, schraubrahmen, seite=None, eben=None):
        if fluegel == "einflügelig":
            if schraubrahmen == "mit schraubrahmen":
                return "Ihre Empfehlung: Produkt 3"
            else:
                return "Ihre Empfehlung: Produkt 1"
        elif fluegel == "zweiflügelig":
            if schraubrahmen == "mit schraubrahmen":
                if seite == "rechts":
                    return "Ihre Empfehlung: Produkt 6"
                elif seite == "links":
                    return "Ihre Empfehlung: Produkt 7"
            else:
                if eben == "ja":
                    if seite == "rechts":
                        return "Ihre Empfehlung: Produkt 8"
                    elif seite == "links":
                        return "Ihre Empfehlung: Produkt 7"
                else:
                    return "Ihre Empfehlung: Produkt 5"

    def frage_balkontuer(schrauben, bedingungen=None, seite=None):
        if schrauben == "mit schrauben":
            return "Ihre Empfehlung: Produkt 3"
        elif schrauben == "ohne schrauben":
            if bedingungen == "ja":
                if seite == "rechts":
                    return "Ihre Empfehlung: Produkt 8"
                elif seite == "links":
                    return "Ihre Empfehlung: Produkt 7"
            else:
                return "Ihre Empfehlung: Produkt 1"

    def frage_fenster(schrauben, typ=None, ausrichtung=None, bedingungen=None):
        if schrauben == "mit schrauben":
            if typ == "einflügelig":
                if ausrichtung == "horizontal":
                    return "Ihre Empfehlung: Produkt 3"
                elif ausrichtung == "vertikal":
                    return "Ihre Empfehlung: Produkt 6"
            elif typ == "zweiflügelig":
                return "Ihre Empfehlung: Produkt 4"
        elif schrauben == "ohne schrauben":
            if bedingungen == "ja":
                if typ == "einflügelig":
                    if ausrichtung == "horizontal":
                        return "Ihre Empfehlung: Produkt 1"
                    elif ausrichtung == "vertikal":
                        return "Ihre Empfehlung: Produkt 2"
                elif typ == "zweiflügelig":
                    return "Ihre Empfehlung: Produkt 4"
            else:
                return "Ihre Empfehlung: Produkt 1"

    if kategorie == "sonnenschutz":
        return jsonify({"empfehlung": frage_sonnenschutz(data.get("fluegel"))})
    elif kategorie == "dachfenster":
        return jsonify({"empfehlung": frage_dachfenster(data.get("verstaerkung"), data.get("fluegel"))})
    elif kategorie == "terrassentuer":
        return jsonify({"empfehlung": frage_terrassentuer(data.get("fluegel"), data.get("schraubrahmen"), data.get("seite"), data.get("eben"))})
    elif kategorie == "balkontuer":
        return jsonify({"empfehlung": frage_balkontuer(data.get("schrauben"), data.get("bedingungen"), data.get("seite"))})
    elif kategorie == "fenster":
        return jsonify({"empfehlung": frage_fenster(data.get("schrauben"), data.get("typ"), data.get("ausrichtung"), data.get("bedingungen"))})
    else:
        return jsonify({"empfehlung": "Ungültige Kategorie"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
