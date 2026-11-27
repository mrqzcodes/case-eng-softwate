# Pontos de falha encontrados:

ADICIONAR AS EVIDENCIAS AQUI.
CRIAR README DO QUE FOI DESENVOLVIDO POR IA E DO QUE FOI FEITO MANUALMENTE

## No processo:
    1. Em caso de falha no script de importação, nada é retornado para o operador e ele apenas roda o script novamente;
    2. O operador realiza todas as operações de salvamento e comparação de dados manualmente, analisando por dado, deixando brechas para eventuais falhas humanas;
    3. Quando um evento não é importado, o script não faz nenhuma notificação, geração de log ou armazenamento do evento que falhou, apenas ignora o evento e segue para o próximo;

## Dados:
    1. Formato das datas despadronizados;
    2. Pagamentos com valor despadronizados;
    3. Pagamentos com valores nulos e negativos;
    4. Eventos de pagamento sendo processados mais de uma vez;

# Melhorias
    1. Ajustar o DB para que eventos de pagamento não aconteçam mais de uma vez, tornando a aplicação idempotente