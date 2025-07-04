from utils.launcher import launch

def open_website(site_key):
    sites = {
        "browser": ("https://www.google.com", "Tarayıcı"),
        "youtube": ("https://www.youtube.com", "YouTube"),
        "github": ("https://github.com", "GitHub"),
        "linkedin": ("https://linkedin.com", "Linkedin"),
        "instagram": ("https://instagram.com", "Instagram"),

    }

    if site_key in sites:
        url, name = sites[site_key]
        launch(url, name, is_web=True)
