# COMANDOS DO MYSQLALCHEMY

### 👉 `flask db init`
- Cria a pastinha que vai cuidar das versões do banco.
- Só faz isso 1 vez no projeto.

### 👉 `flask db migrate -m "mensagem do migrate"`
- Olha pros modelos que você criou e gera um rascunho das mudanças no banco.
- Mas ainda NÃO mexe no banco de verdade.
- É semelhante ao `git add` + `git commit`, mas pro banco.

### 👉 `flask db upgrade`
- Agora sim: aplica de verdade as mudanças no banco.
- Tipo: cria tabelas, colunas, essas paradas.

### 👉 `flask run`
- Liga o servidor.
- Agora dá pra acessar seu site/API no navegador.