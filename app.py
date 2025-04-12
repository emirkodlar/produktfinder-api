from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/produktfinder", methods=["POST"])
def produktfinder():
    data = request.json
    kategorie = data.get("kategorie")

    def frage_sonnenschutz(fluegel):
        if fluegel == "einflügelig":
            return "Ihre Empfehlung: Produkt 12"
        elif fluegel == "zweiflügelig":
            return "Ihre Empfehlung: Produkt 10"

    def frage_dachfenster(verdunkelung, fluegel=None):
        if verdunkelung == "mit verdunkelung":
            return "Ihre Empfehlung: Produkt 11"
        elif verdunkelung == "ohne verdunkelung":
            if fluegel == "einflügelig":
                return "Ihre Empfehlung: Produkt 6"
            elif fluegel == "zweiflügelig":
                return "Ihre Empfehlung: Produkt 9"

    def frage_terrassentuer(fluegel, eben, seite=None):
        if fluegel == "einflügelig":
            if eben == "mit schwellenrahmen":
                return "Ihre Empfehlung: Produkt 3"
            elif eben == "eben":
                if seite == "rechts":
                    return "Ihre Empfehlung: Produkt 8"
                elif seite == "links":
                    return "Ihre Empfehlung: Produkt 7"
        elif fluegel == "zweiflügelig":
            if eben == "mit schwellenrahmen":
                return "Ihre Empfehlung: Produkt 4"
            elif eben == "eben":
                if seite == "rechts":
                    return "Ihre Empfehlung: Produkt 8"
                elif seite == "links":
                    return "Ihre Empfehlung: Produkt 7"

    def frage_balkontuer(schrauben, schwelle=None, seite=None, bedingung=None):
        if schrauben == "mit schrauben":
            if schwelle == "mit schwelle":
                return "Ihre Empfehlung: Produkt 3"
            elif schwelle == "ohne schwelle":
                if seite == "rechts":
                    return "Ihre Empfehlung: Produkt 8"
                elif seite == "links":
                    return "Ihre Empfehlung: Produkt 7"
        elif schrauben == "ohne schrauben":
            if bedingung == "ja":
                if seite == "rechts":
                    return "Ihre Empfehlung: Produkt 8"
                elif seite == "links":
                    return "Ihre Empfehlung: Produkt 7"
            else:
                if schwelle == "mit schwelle":
                    return "Ihre Empfehlung: Produkt 3"
                elif schwelle == "ohne schwelle":
                    if seite == "rechts":
                        return "Ihre Empfehlung: Produkt 8"
                    elif seite == "links":
                        return "Ihre Empfehlung: Produkt 7"

    def frage_fenster(schrauben, typ=None, richtung=None, bedingung=None):
        if schrauben == "mit schrauben":
            if typ == "einflügelig":
                if richtung == "horizontal":
                    return "Ihre Empfehlung: Produkt 3"
                elif richtung == "vertikal":
                    return "Ihre Empfehlung: Produkt 6"
            elif typ == "zweiflügelig":
                return "Ihre Empfehlung: Produkt 4"
        elif schrauben == "ohne schrauben":
            if bedingung == "ja":
                if richtung == "horizontal":
                    return "Ihre Empfehlung: Produkt 1"
                elif richtung == "vertikal":
                    return "Ihre Empfehlung: Produkt 2"
            else:
                if typ == "einflügelig":
                    if richtung == "horizontal":
                        return "Ihre Empfehlung: Produkt 3"
                    elif richtung == "vertikal":
                        return "Ihre Empfehlung: Produkt 6"
                elif typ == "zweiflügelig":
                    return "Ihre Empfehlung: Produkt 4"

    if kategorie == "sonnenschutz":
        return jsonify({"empfehlung": frage_sonnenschutz(data.get("fluegel"))})
    elif kategorie == "dachfenster":
        return jsonify({"empfehlung": frage_dachfenster(data.get("verdunkelung"), data.get("fluegel"))})
    elif kategorie == "terrassentuer":
        return jsonify({"empfehlung": frage_terrassentuer(data.get("fluegel"), data.get("eben"), data.get("seite"))})
    elif kategorie == "balkontuer":
        return jsonify({"empfehlung": frage_balkontuer(data.get("schrauben"), data.get("schwelle"), data.get("seite"), data.get("bedingung"))})
    elif kategorie == "fenster":
        return jsonify({"empfehlung": frage_fenster(data.get("schrauben"), data.get("typ"), data.get("richtung"), data.get("bedingung"))})
    else:
        return jsonify({"empfehlung": "Ungültige Kategorie"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
