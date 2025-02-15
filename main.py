import os
import google.generativeai as genai
from dotenv import load_dotenv

#carregar chave de API do arquivo .env para variável de ambiente
load_dotenv()
api_key = os.getenv("SUA_CHAVE")

genai.configure(api_key=api_key)

prompts = {
    "resumo": "Resuma o seguinte assunto de forma clara e objetiva:\n\n{entrada}",
    "explicacao_simples": "Explique de forma simples e didática para um iniciante:\n\n{entrada}",
    "geracao_de_ideias": "Gere ideias criativas sobre o seguinte tema:\n\n{entrada}",
    "traducao": "Traduza o seguinte texto para inglês:\n\n{entrada}"
}


def GerarResposta(opcao, entrada):
    """Gera a resposta baseada no prompt pré-pronto e na entrada do usuário."""
    if opcao in prompts:
        prompt_escolhido = prompts[opcao].format(entrada=entrada)

        # Gerar a resposta com o Gemini
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt_escolhido)

        # Verificar se a resposta contém texto antes de acessá-lo
        return response.text if hasattr(response, "text") else "⚠️ Erro ao gerar resposta."
    else:
        return "❌ Opção inválida. Escolha entre: " + ", ".join(prompts.keys())
    
# Interface de escolha do usuário
print("\n🎯 Escolha uma opção:")
for key in prompts.keys():
    print(f"- {key}")

while True:
    opcao = input("\nDigite a opção desejada: ").strip().lower()
    if opcao in prompts:
        break
    print("❌ Opção inválida. Tente novamente.")

entrada_usuario = input("\nDigite o tema: ").strip()
resposta = GerarResposta(opcao, entrada_usuario)
print("\n🤖 Resposta da IA:\n", resposta)

