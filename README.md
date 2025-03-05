# API de Cadastro de E-mails para Fatura Eletrônica

## 📌 Visão Geral
Esta API foi desenvolvida para permitir que clientes cadastrem seus e-mails para recebimento de faturas eletrônicas em um ambiente autenticado. A solução visa modernizar o processo de faturamento, proporcionando maior conveniência para os clientes e reduzindo o uso de papel.

## 🎯 Necessidade Atendida
A equipe de atendimento ao cliente identificou a demanda de clientes que desejam receber suas faturas eletronicamente. Para atender a essa necessidade, foi criada esta API RESTful, que possibilita o cadastro seguro de e-mails, garantindo a validação correta dos dados e a conformidade com as melhores práticas de desenvolvimento.

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python
- **Framework**: Flask
- **Banco de Dados**: Banco de Dados SQLite com SQLAlchemy
- **Validação de Dados**: Marshmallow
- **Documentação**: OpenAPI/Swagger
- **Gerenciamento de Versionamento**: Git e GitHub
- **Ambiente de Desenvolvimento**: Docker (planejado para versões futuras)

## 🔍 Estrutura da API
A API segue o padrão RESTful e utiliza os seguintes endpoints:

### 1️⃣ Cadastro de E-mail
**Rota**: `POST /cadastrar-email`
- Recebe um JSON com um endereço de e-mail válido
- Realiza a validação e armazena no banco de dados
- Retorna status `201 Created` em caso de sucesso

### 2️⃣ Consulta de E-mail
**Rota**: `GET /emails`
- Retorna todos os e-mails cadastrados
- Possui paginação para otimizar as respostas

### 3️⃣ Atualização de E-mail
**Rota**: `PUT /atualizar-email/{id}`
- Permite a atualização completa do e-mail cadastrado
- Retorna status `200 OK` em caso de sucesso

### 4️⃣ Exclusão de E-mail
**Rota**: `DELETE /deletar-email/{id}`
- Remove o e-mail cadastrado
- Retorna `204 No Content` caso a exclusão seja bem-sucedida

## 📌 Próximas Melhorias
Esta é uma versão inicial da API. Algumas melhorias previstas incluem:
- **Autenticação e Autorização**: Implementação de OAuth 2.0 ou JWT para garantir maior segurança.
- **Monitoramento**: Integração com Sensedia para acompanhar métricas de uso e performance.
- **Ambiente de Produção**: Configuração de um pipeline CI/CD para facilitar a implantação automatizada.
- **Notificações**: Implementação de envio de confirmação por e-mail após o cadastro.
- **Cache**: Uso de Redis para otimizar consultas frequentes.
- **Suporte a Webhooks**: Para notificações em tempo real sobre mudanças nos cadastros.

## 📜 Contribuição
Contribuições são bem-vindas! Caso tenha sugestões ou queira colaborar, siga os passos abaixo:
1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b minha-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adicionando nova feature'`).
4. Envie um push (`git push origin minha-feature`).
5. Abra um Pull Request.

## 📩 Contato
Caso tenha dúvidas ou precise de suporte, entre em contato através do e-mail: mbnunes2025@outlook.com.

---
🚀 API em constante evolução para oferecer um serviço mais eficiente e seguro para os clientes!

