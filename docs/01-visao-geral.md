# Ticket WorkFlow

> Sistema web para gerenciamento de chamados técnicos e ativos de TI.

---

# Visão Geral

O Ticket Worflow é um aplicativo web desenvolvido para centralizar o gerenciamento de chamados técnicos, permitindo acompanhar todo o ciclo de atendimento, desde a abertura da solicitação até sua conclusão, mantendo o histórico completo de cada atendimento.

Além do gerenciamento de chamados, o sistema possibilita o controle de usuários, organização da equipe de suporte e disponibilização de Informações gerenciais por meio de dashboards.

O projeto foi desenvolvido com o objetivo de aplicar boas práticas de desenvolvimento de software, utilizando ASP.NET Core MVC, C#, Entity Framework Core e SQL Server, simulando um ambiente corporativo.

# Problema

Em empresas com grande volume de solicitações de suporte, é comum que os chamados sejam registrados por diferentes canais, como e-mail, telefone, aplicativos de mensagens ou até mesmo de forma verbal.

Esse processo dificulta a organização das demandas, aumenta o tempo de resposta, compromete o acompanhamento das solicitações e pode ocasionar perda de histórico de atendimento.

Além disso, a ausência de um sistema centralizado dificulta a definição de prioridades, o gerenciamento de atendimentos urgentes e a análise do desempenho da equipe de suporte.

O Ticket Workflow foi idealizado para resolver esses desafios, centralizando todas as solicitações em uma única plataforma, permitindo maior organização, rastreabilidade e a eficiência no processo de atendimento.

# Objetivo 

Desenvolver uma aplicação web para gerenciamento de chamados e ativos de TI, proporcionando maior organização, rastreabilidade e eficiência no atendimento às solicitações dos usuários.

O sistema permitirá o registro, acompanhamento e gerenciamento de chamados, oferecendo uma interface intuitiva para usuários, técnicos e administradores. Além disso, disponibilizará indicadores e informações gerenciais que auxiliem na tomada de decisão e no monitoramento do desempenho da equipe de suporte.

# Público-Alvo

O Ticket WorkFlow foi desenvolvido para empresas que possuem uma equipe interna de Tecnologia da Informação e necessitam organizar o fluxo de atendimento de chamados técnicos.

O sistema atenderá diferentes perfis de usúarios, cada um com responsabilidade específicas:

- **Usuário:** registra chamados, acompanha o andamento e interage com a equipe de suporte.
- **Técnico:** visualiza os chamados disponíveis, assume atendimentos, registra atualizações e conclui as solicitações.
- **Administração:** gerencia usuários, departamentos, categorias, equipes, permissões e acompanham indicadores por meio de dashboards.

# Tecnologias

O Ticket WorkFlow será desenvolvido utilizando tecnologias modernas do ecossistema Microsoft, com foco em boas práticas de desenvolvimento, organização do código e escalabilidade.

As principais tecnologias utilizadas serão:

- ASP.NET Core MVC (.NET 8)
- C#
- Entity Framework Core
- SQL Server 
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Git
- GitHub
- Visual Studio 2022
- Visual Studio Code 

## Escopo da Versão 1.0

A primeira versão do Titcket WorkFlow contemplará as seguintes funcionalidades:

### Autenticação 
- Login de usuários.
- Logout.
- Controle de perfils (Usuários, Técnico e Administração).

### Gestão de Usuários
- Cadastro de usuários
- Edição de usuários.
- Ativação e inativação de usuários.

### Administração
- Cadastro de departamento.
- Cadastro de categorias de chamados.
- Cadastro de prioridades.

### Gestão de Chamados
- Abertura de chamados 
- Visualização da fila de atendimento.
- Atribuição de chamados aos técnicos.
- Alteração de status.
- Registro de comentários.
- Histórico de movimentações.

### Gestão de Ativos
- Gestão de ativos de TI.
- Vinculação de equipamentos aos usuários.
- Consulta ao histórico de chamados por equipamentos.

### Dashboard Gerencial
- Indicadores de chamados por status.
- Indicadores por prioridade.
- Indicadores por departamento.
- Indicadores por técnico.

# Escopo Futuro 

As funcionalidades abaixo estão previstas para versões futuras do Ticket WorkFlow:

- Controle de SLA (Acordo de Nível de Serviço).
- Upload de anexos em chamados.
- Notificações automáticas por e-mail.
- Base de conhecimento para consulta de soluções.
- Relatórios gerenciais avançados.
- Distribuição automática de chamados entre técnicos.
- Pesquisa de satisfação ao encerramento do atendimento.
- Integração com Microsoft Teams e Slack.
- Aplicação responsiva para dispositivos móveis.
- Assistente com Inteligência Artificial para sugerir soluções com base no histórico de chamados.
- Autenticação de dois fatores (2FA).
- Exportação de relatórios em PDF e Excel.
- Auditoria de ações dos usuários.
