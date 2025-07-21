# Language prompts for different locales
LANGUAGE_PROMPTS = {
    "English": "You are a data analyst. Provide clear insights.",
    "French": "Vous êtes un analyste de données. Fournissez des analyses claires en français.",
    "Spanish": "Eres un analista de datos. Proporciona análisis claros en español.",
    "German": "Sie sind ein Datenanalyst. Geben Sie klare Analysen auf Deutsch.",
    "Italian": "Sei un analista di dati. Fornisci analisi chiare in italiano.",
    "Portuguese": "Você é um analista de dados. Forneça insights claros em português."
}

# Supported languages list (automatically generated from prompts)
SUPPORTED_LANGUAGES = list(LANGUAGE_PROMPTS.keys())

# Default language fallback
DEFAULT_LANGUAGE = "English"