import nltk
import random
import pyttsx3

# Inicializa a voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade da fala
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')  # Voz feminina (macOS)
# Para Windows, use: 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH_OneCore\Voices\Tokens\MSTTS_V110_ptBR_Maria'

# Banco de palavras e frases para ensino
palavras = {
    "amor": "love",
    "amizade": "friendship",
    "livro": "book",
    "casa": "house",
    "feliz": "happy",
    "trabalho": "work",
    "rápido": "fast",
    "devagar": "slow",
    "inteligente": "smart",
    "lindo": "beautiful"
}

frases = {
    "Eu gosto de estudar.": "I like to study.",
    "Ela tem um gato.": "She has a cat.",
    "Nós vamos para a escola.": "We go to school.",
    "Ele está muito feliz hoje.": "He is very happy today.",
    "Você fala inglês?": "Do you speak English?"
}


# Função para falar
def falar(texto):
    engine.say(texto)
    engine.runAndWait()


# Função para ensinar palavras
def ensinar_palavra():
    palavra, traducao = random.choice(list(palavras.items()))
    print(f"📖 Como se diz '{palavra}' em inglês?")
    falar(f"How do you say {palavra} in English?")

    resposta = input("Sua resposta: ").strip().lower()
    if resposta == traducao:
        print("✅ Correto! Muito bem! 🎉")
        falar("Correct! Well done!")
    else:
        print(f"❌ Errado. A resposta certa é '{traducao}'.")
        falar(f"Wrong. The correct answer is {traducao}.")


# Função para ensinar frases
def ensinar_frase():
    frase_pt, frase_en = random.choice(list(frases.items()))
    print(f"📝 Traduza a frase: '{frase_pt}' para o inglês.")
    falar(f"Translate the sentence: {frase_pt}")

    resposta = input("Sua resposta: ").strip().lower()
    if resposta == frase_en.lower():
        print("✅ Ótimo! Você acertou! 🎉")
        falar("Great! You got it right!")
    else:
        print(f"❌ Não foi dessa vez. A resposta correta é: '{frase_en}'.")
        falar(f"Not this time. The correct answer is {frase_en}.")


# Função principal
def iniciar_professora():
    print("👩‍🏫 Olá! Eu sou sua professora de inglês virtual! 🇬🇧 Vamos aprender juntos!")
    falar("Hello! I am your virtual English teacher! Let's learn together!")

    while True:
        print("\n📚 Escolha uma opção:")
        print("1️⃣ Aprender palavras")
        print("2️⃣ Aprender frases")
        print("3️⃣ Sair")
        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            ensinar_palavra()
        elif opcao == "2":
            ensinar_frase()
        elif opcao == "3":
            print("👋 Até logo! Continue praticando inglês! 🇬🇧")
            falar("Goodbye! Keep practicing English!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")


# Iniciar a professora IA
if __name__ == "__main__":
    iniciar_professora()
