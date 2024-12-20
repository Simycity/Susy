# Importa a biblioteca
import speech_recognition as sr

# Cria um reconhecedor
r = sr.Recognizer()

# Tenta capturar áudio do microfone
try:
    with sr.Microphone() as source:
        print("Ajustando para ruído ambiente... Aguarde.")
        r.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
        print("Fale algo: ")
        audio = r.listen(source)  # Escuta o áudio do microfone

    # Reconhece o áudio usando o Google Speech Recognition
    print("Você disse: " + r.recognize_google(audio, language="pt-BR"))

except sr.UnknownValueError:
    print("Desculpe, não consegui entender o que foi dito.")

except sr.RequestError as e:
    print(f"Erro ao se comunicar com o serviço de reconhecimento: {e}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")