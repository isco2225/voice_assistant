import wikipedia
from wikipedia.exceptions import PageError, DisambiguationError

def fetch_wikipedia_summary(query, lang="tr"):
    wikipedia.set_lang(lang)
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except DisambiguationError as e:
        return f"Bu kelime çok anlamlı olabilir: {', '.join(e.options[:3])}"
    except PageError:
        return "Bu konuda bir bilgi bulunamadı."
    except Exception as e:
        return f"Arama sırasında bir hata oluştu: {str(e)}"
