# Bookberry - Sistema de Gerenciamento de Acervo de Livros

## Descrição
Bookberry é uma aplicação web desenvolvida em Python com o framework Django, projetada para facilitar o gerenciamento de um acervo de livros. Com Bookberry, você pode pesquisar, inserir, visualizar, deletar e editar informações sobre livros de forma eficiente e organizada.

## Tecnologias Utilizadas
- Python
- Django
- PostgreSQL

## Funcionalidades Principais
- **Pesquisa:** Encontre rapidamente livros utilizando a função de pesquisa.
- **Inserção:** Adicione novos livros ao acervo de forma intuitiva e fácil.
- **Visualização:** Veja detalhes completos sobre os livros armazenados.
- **Deleção:** Remova livros do acervo quando necessário.
- **Edição:** Atualize as informações dos livros conforme necessário.

## Requisitos de Instalação
Certifique-se de ter o Python e o PostgreSQL instalados em seu sistema antes de prosseguir.

1. Clone o repositório do GitHub:
    ```
    git clone https://github.com/seu-usuario/bookberry.git
    ```
2. Acesse o diretório do projeto:
    ```
    cd bookberry
    ```
3. Instale as dependências usando pip:
    ```
    pip install -r requirements.txt
    ```
4. Configure as variáveis de ambiente para conexão com o banco de dados PostgreSQL.

## Configuração do Banco de Dados
Certifique-se de configurar corretamente o banco de dados PostgreSQL antes de executar o aplicativo. Você pode fazer isso atualizando as configurações do banco de dados no arquivo `.env`.

## Executando a Aplicação
Após concluir a configuração do banco de dados e fazer as migrações, você pode iniciar a aplicação Django usando o seguinte comando:
```
python manage.py runserver
```

Acesse a aplicação em seu navegador, geralmente disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, correções de bugs ou novas funcionalidades que você gostaria de ver implementadas.
