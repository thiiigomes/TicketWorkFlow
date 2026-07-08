# Casos de Uso

## Objetivo 

Este documento descreve os principais fluxos de utilização do sistema Ticket WorkFlow.

Cada caso de uso representa uma interação entre um usuário e o sistema, descrevendo as etapas necessárias para a execução de uma funcionalidade.

## UC001 - Abrir Chamado

**Ator Principal:** Usuário

**Objetivo:**
Permitir que um usuário registre um novo chamado de suporte.

**Pré-condições:**
- O usuário deve estar autenticado no sistema.

**Observação:**
- Durante a abertura do chamado, os campos exibidos variam conforme a categoria selecionada, conforme definido na RN010.

**Fluxo Principal:**

1. O usuário acessa a tela de abertura de chamados.
2. O sistema apresenta o formulário de abertura.
3. O usuário seleciona a categoria do problema.
4. O sistema exibe os campos específicos conforme a categoria.
5. O usuário preenche as informações solicitadas.
6. O usuário envia o chamado.
7. O sistema registra o chamado.
8. O sistema define o status do chamado como **Aberto**.
9. O sistema coloca o chamado na fila de atendimento.
10. O sistema confirma a abertura do chamado.

**Pós-condições:**

- O chamado é criado com sucesso.
- O chamado fica disponível para atendimento.
- O chat do chamado é criado automaticamente para permitir a comunicação entre usuário e técnico durante o atendimento.

## UC002 - Assumir Chamado 

**Ator Principal:** Técnico

**Objetivo:**
Permitir que um técnico assuma um chamado para iniciar o atendimento.

**Pré-condições:**

- O técnico deve estar autenticado no sistema.
- O chamado deve possuir o status **Aberto**.
- O chamado não poderá possuir outro técnico responsável.

**Observação:**

- Apenas um técnico poderá assumir um chamado por vez, conforme definido na RN006.

**Fluxo Principal:**

1. O técnico acessa a fila de chamados.
2. O sistema exibe todos os chamados disponíveis para atendimento.
3. O técnico seleciona um chamado.
4. O sistema apresenta todas as informações do chamado.
5. O técnico analisa o problema relatado.
6. Caso necessário, o técnico solicita informações adicionais ao usuário por meio do chat do chamado.
7. O técnico clica na opção **Assumir Chamado**.
8. O sistema verifica se o chamado continua disponível.
9. O sistema vincula o chamado ao técnico responsável.
10. O sistema altera o status do chamado para **Em Atendimento**.
11. O sistema registra a data, hora e o responsável pelo atendimento.
12. O sistema confirma a atribuição ao técnico responsável.

**Fluxos Alternativos:**

**FA01**

No passo 8, caso outro técnico já tenha assumido o chamado, o sistema deverá informar que o chamado não está mais disponível para atendimento.

**FA02**

No passo 6, caso o técnico solicite informações adicionais ao usuário, o sistema deverá alterar o status do chamado e aguarda o retorno do usuário para prosseguir com o atendimento.

Após o usuário responder, o sistema deverá retornar automaticamente o status para **Em Atendimento**.

**Pós-condições:**

- O chamado ficará vinculado ao técnico responsável.
- O atendimento poderá ser iniciado.
- Todas as movimentações deverão permanecer registradas no histórico do chamado.

**Regras de Negócio Relacionadas:**

- RN001
- RN002
- RN006
- RN013
- RN020
- RN021

## UC003 - Atualizar Chamado

**Ator Principal:** Técnico

**Objetivo:**
Permitir que o técnico registre as atividades realizadas durante o atendimento e mantenha o chamado atualizado.

**Pré-condições:**

- O técnico deve estar autenticado.
- O chamado deve estar vinculado ao técnico responsável.
- O chamado deve possuir o status **Em Atendimento**.

**Observação:**

- O registro detalhado da solução deverá ser realizado ao final do atendimento.
- O sistema registrará automaticamente todas as alterações de status do chamado.

**Fluxo Principal:**

1. O técnico acessa o chamado em atendimento.
2. O sistema apresenta todas as informações do chamado.
3. O técnico realiza o diagnóstico do problema.
4. Caso necessário, o técnico altera o status do chamado conforme o andamento do atendimento.
5. O técnico poderá trocar mensagens com o usuário pelo chat do chamado.
6. O técnico poderá anexar imagens ou arquivos relacionados ao atendimento.
7. Caso ocorra substituição de equipamento ou componente, o técnico registra o item substituído, o motivo da substituição e, quando aplicável, o patrimônio ou número de série do novo equipamento.
8. Após concluir o atendimento, o técnico registra a solução aplicada.
9. O sistema grava todas as informações no histórico do chamado.
10. O sistema mantém o chamado atualizado para futuras consultas.

**Fluxos Alternativos:**

**FA01**

Caso o técnico necessite de informações adicionais do usuário, o sistema deverá alterar o status para **Aguardando Usuário**.

Após a resposta do usuário, o sistema deverá retornar automaticamente o status para **Em Atendimento**.

**FA02**

Caso seja necessário anexar evidências do atendimento, o sistema deverá permitir o envio de imagens ou documentos.

**Pós-condições:**

- O histórico do chamado permanece atualizado.
- As alterações realizadas ficam registradas.
- O chamado permanece disponível para continuidade do atendimento.

**Regras de Negócio Relacionadas:**

- RN008
- RN009
- RN013
- RN019
- RN020
- RN021

## UC004 - Encerrar Chamado

**Ator Principal:** Técnico 

**Objetivo:**
Permitir que o técnico finalize um chamado após a conclusão do atendimento.

**Pré-condições:**

- O técnico deve estar autenticado no sistema.
- O chamado deve estar vinculado ao técnico responsável.
- O chamado deve possuir o status **Em Atendimento**

**0bservação:**

- Somente o técnico responsável poderá encerrar chamado.

**Fluxo Principal:**

1. O técnico acessa o chamado em atendimento.
2. O sistema apresenta todas as informações do chamado.
3. O técnico registra a solução aplicada.
4. Caso tenha ocorrido substituição de equipamento ou componente, o técnico registra o item substituído.
5. O técnico adicona observações finais do atendimento.
6. O técnico seleciona a opção **Encerrar Chamado**.
7. O sistema verifica se todas as informações obrigatórias foram preenchidas.
8. O sistema registra automaticamente a data, hora e o tempo total do atendimento.
10. O sistema notifica o usuário sobre o encerramento do chamado,
11. O sistema disponibiliza, opcionalmente, um campo para que o usuário registre um comentário sobre o atendimento.
12. Caso o problema persiste, o usuário poderá solicitar a reabertura do chamado.

**Fluxos Alternstivos:**

**FA01**

Caso as informações obrigatórias não tenham sido preenchidas, o sistema deverá impedir o encerramento do chamado e informar os campos pendentes.

**FA02**

Caso o uduário solicite a reabertura do chamado, o sistema deverá restaurar o status para **Em Atendimento**, manter todo o histórico do atendimento anterior e notificar automaticamente o gestor responsável.

**Pós-condições:**

- O chamado permanece encerrado para consulta.
- Todo histórico permanece registrado.
- O usuário poderá consultar a solução aplicada.
- O comentário do usuário, quando informado, ficará registrado no histórico.

**Regras de Negócio Relacionadas:**

- RN006
- RN012
- RN013
- RN021
- RN022
- RN023