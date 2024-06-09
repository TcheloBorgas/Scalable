#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
from factory import create_app
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

app = create_app()

if __name__ == '__main__':
    try:
        app.run(debug=False) 
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")