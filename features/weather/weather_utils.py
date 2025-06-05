import random

def describe_weather_code(code: int) -> str:
    weather_descriptions = {
        0: "açık ve güneşli",
        1: "çoğunlukla güneşli",
        2: "parçalı bulutlu",
        3: "bulutlu",
        45: "sisli",
        48: "buz sisi var",
        51: "hafif çiseleme var",
        53: "orta şiddette çiseleme var",
        55: "yoğun çiseleme var",
        61: "hafif yağmur var",
        63: "orta şiddette yağmur var",
        65: "yoğun yağmur var",
        71: "hafif kar yağıyor",
        73: "orta kar yağışı var",
        75: "yoğun kar yağıyor",
        95: "fırtına var",
        96: "fırtına ve hafif dolu var",
        99: "fırtına ve yoğun dolu var"
    }

    return weather_descriptions.get(code, "durumu bilinmiyor")



def generate_weather_advice(temperature: float) -> str:
    if temperature >= 28:
        options = [
            "Bugün hava oldukça sıcak. Bol su içmeni öneririm.",
            "Güneşli bir gün serin yerlerde kalmaya çalış.",
            "Sıcaklara dikkat Hafif ve açık renkli kıyafetler giy."
        ]
    elif 20 <= temperature < 28:
        options = [
            "Hava güzel. Hafif bir kıyafet tercih edebilirsin.",
            "Tam gezmelik bir hava. Tişört yeterli olabilir.",
            "Ne sıcak ne soğuk, dışarısı oldukça keyifli görünüyor."
        ]
    elif 10 <= temperature < 20:
        options = [
            "Hava serin. Dışarı çıkarken ince bir ceket almayı unutma.",
            "Serin bir hava var. Üşümemek için katlı giyinmeyi düşün.",
            "Mont olmasa da bir hırka iş görür."
        ]
    else:
        options = [
            "Hava oldukça soğuk. Kalın giyinmeni tavsiye ederim.",
            "Soğuk bir gün. Eldiven ve bere almayı unutma.",
            "Titrememek için kat kat giyinmek iyi olabilir."
        ]

    return random.choice(options)

