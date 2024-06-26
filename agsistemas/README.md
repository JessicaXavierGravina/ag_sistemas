
# Projeto Django de Controle de Veículos e Motoristas *

Este é um projeto Django para gerenciar veículos, motoristas e seus controles de saída e retorno.

## Instalação

1. Clone o repositório para sua máquina local:
   ```
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
   
2. Instale as dependências do projeto:
   ```
   pip install -r requirements.txt
   ```

## Configuração do Banco de Dados

Certifique-se de configurar o banco de dados conforme necessário no arquivo `settings.py`. Aqui está um exemplo de configuração usando MySQL:

   ```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd_agsistemas',
        'USER': 'agsistemas',
        'PASSWORD': 'sistemasag',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
   ```

## Executando o Servidor de Desenvolvimento

Para iniciar o servidor de desenvolvimento, execute o seguinte comando na raiz do projeto:

   ```
python manage.py runserver
   ```

O servidor estará acessível em [http://localhost:8000](http://localhost:8000).

## Funcionalidades

### Página Inicial

A página inicial exibe estatísticas básicas sobre veículos e motoristas cadastrados.

### Controle

- **Listar Controles:** Exibe todos os controles de saída e retorno de veículos.
- **Criar Controle:** Permite criar um novo controle de saída e retorno de veículo.
- **Editar Controle:** Permite editar um controle existente.
- **Excluir Controle:** Permite excluir um controle existente.
- **Detalhes do Controle:** Exibe detalhes de um controle específico.

### Veículos

- **Listar Veículos:** Exibe todos os veículos cadastrados.
- **Criar Veículo:** Permite criar um novo veículo.
- **Editar Veículo:** Permite editar um veículo existente.
- **Excluir Veículo:** Permite excluir um veículo existente.
- **Detalhes do Veículo:** Exibe detalhes de um veículo específico, incluindo seus controles associados.

### Motoristas

- **Listar Motoristas:** Exibe todos os motoristas cadastrados.
- **Criar Motorista:** Permite criar um novo motorista.
- **Editar Motorista:** Permite editar um motorista existente.
- **Excluir Motorista:** Permite excluir um motorista existente.
- **Detalhes do Motorista:** Exibe detalhes de um motorista específico, incluindo os controles associados.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar pull requests com melhorias.
