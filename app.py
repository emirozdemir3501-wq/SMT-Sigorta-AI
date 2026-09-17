from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").lower().strip()

    if any(word in question for word in [
        "kasko", "araç sigortası", "araba sigortası"
    ]):
        answer = """🚗 Kasko Sigortası

Kasko; aracınızı kaza, hırsızlık, yangın ve poliçenizde belirtilen diğer risklere karşı güvence altına alabilir.

Teminatlar poliçeye göre değişebilir. 📄"""

    elif any(word in question for word in [
        "trafik sigortası", "zorunlu trafik"
    ]):
        answer = """🚘 Trafik Sigortası

Zorunlu trafik sigortası, aracınızla üçüncü kişilere verebileceğiniz maddi ve bedeni zararlar için güvence sağlar.

Teminat ve limitler poliçeye göre değişebilir."""

    elif any(word in question for word in [
        "konut", "ev sigortası", "evimi"
    ]):
        answer = """🏠 Konut Sigortası

Konut sigortası; evinizi ve poliçenizde belirtilen eşyaları yangın, hırsızlık, su baskını gibi çeşitli risklere karşı güvence altına alabilir."""

    elif any(word in question for word in [
        "sağlık", "hastane", "muayene"
    ]):
        answer = """🏥 Sağlık Sigortası

Sağlık sigortası, poliçedeki şartlara bağlı olarak muayene, tedavi ve bazı sağlık hizmetlerinin masraflarını karşılayabilir."""

    elif any(word in question for word in [
        "seyahat", "yurt dışı", "uçak"
    ]):
        answer = """✈️ Seyahat Sigortası

Seyahat sigortası; poliçeye bağlı olarak sağlık giderleri, bagaj sorunları ve seyahat sırasında oluşabilecek bazı riskleri kapsayabilir."""

    elif any(word in question for word in [
        "hasar", "kaza", "çarpışma"
    ]):
        answer = """💥 Hasar

Hasar durumunda öncelikle güvenliğinizi sağlayın ve poliçenizde belirtilen hasar bildirim prosedürünü takip edin.

Gerekli belgeler ve süreç sigorta türüne göre değişebilir."""

    elif any(word in question for word in [
        "teminat", "karşılıyor", "kapsıyor", "kapsam"
    ]):
        answer = """🛡️ Teminat

Bir sigorta poliçesinin hangi riskleri karşıladığı poliçedeki teminatlara bağlıdır.

Poliçenizi yüklerseniz DEMO sistemimiz üzerinden teminatları inceleyebilirsiniz. 📄"""

    elif any(word in question for word in [
        "poliçe", "police", "poliçem"
    ]):
        answer = """📄 Poliçe

Poliçe, sigorta sözleşmesinin şartlarını ve teminatlarını gösteren belgedir.

Poliçedeki özel şartları ve istisnaları kontrol etmek önemlidir."""

    elif any(word in question for word in [
        "prim", "fiyat", "ücret", "ne kadar"
    ]):
        answer = """💰 Sigorta Primi

Sigorta primi; sigortanın türüne, teminatlara, risklere ve poliçenin diğer şartlarına göre değişebilir."""

    elif any(word in question for word in [
        "iptal", "yenileme", "yenile"
    ]):
        answer = """📅 Poliçe İşlemleri

Poliçe iptali ve yenileme şartları sigorta şirketine ve poliçenin koşullarına göre değişebilir."""

    elif any(word in question for word in [
        "tazminat", "ödeme"
    ]):
        answer = """💳 Tazminat

Tazminat miktarı; oluşan zarara, poliçe teminatlarına, limitlere ve poliçedeki şartlara göre belirlenebilir."""

    elif any(word in question for word in [
        "iletişim", "ulaş", "telefon", "adres", "email", "e-posta"
    ]):
        answer = """📞 İletişim

SMT Sigorta ile iletişim kurmak için aşağıdaki iletişim bölümünü kullanabilirsiniz."""

    elif any(word in question for word in [
        "merhaba", "selam"
    ]):
        answer = """🤖 Merhaba!

Ben SMT Sigorta AI.

Kasko, trafik, konut, sağlık, seyahat, hasar, poliçe ve teminatlar hakkında sorularınızı yanıtlayabilirim."""

    else:
        answer = """🤖 Ben SMT Sigorta AI.

Sigorta ile ilgili sorularınızı yanıtlayabilirim.

🚗 Kasko
🚘 Trafik sigortası
🏠 Konut sigortası
🏥 Sağlık sigortası
✈️ Seyahat sigortası
💥 Hasar
📄 Poliçe
🛡️ Teminat

Lütfen sigortayla ilgili bir soru sorun."""

    return jsonify({"answer": answer})
@app.route("/analyze-policy", methods=["POST"])
def analyze_policy():
    file = request.files.get("policy")

    if not file:
        return jsonify({
            "answer": "Lütfen önce bir PDF poliçe seçin."
        }), 400

    answer = """
## Poliçenin Özeti

Bu belge DEMO amaçlı hazırlanmış örnek bir sigorta poliçesidir.

## Sigortalı

Ahmet Yılmaz

## Araç

2024 Örnek Sedan
Plaka: DEMO 001

## Poliçe Bilgileri

Poliçe No: DEMO-2026-001
Başlangıç: 01.10.2026
Bitiş: 01.10.2027

## Teminatlar

• Kasko
• Hırsızlık
• Yangın
• Doğal afetler

## Muafiyet

5.000 TL

## Önemli Not

Bu analiz DEMO modunda çalışmaktadır.
Gerçek bir sigorta poliçesi yerine geçmez.
"""

    return jsonify({"answer": answer})
    

if __name__ == "__main__":
    app.run(debug=True)