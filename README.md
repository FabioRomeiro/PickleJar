# Pickle Jar

**Autor:** Fábio Romeiro

**Descrição:** Projeto de graduação propondo uma aplicação de gerenciamento de senha sem a necessidade de uma _senha mestra_ para o acesso ao conteúdo do usuário, mas sim uma senha gráfica, que utiliza elementos visuais ao invés da caracteres alfanuméricos. Este projeto será divido em duas aplicações, um aplicativo Android e uma aplicação Web, sendo a Android o sistema "principal", pois a aplicação Web só funcionará enquanto o app Android estiver ativo (tipo Whatsapp Web). 

## Rodando o projeto
Requisito:
- [Docker](https://docs.docker.com/install/)


```bash
source dev.sh  # importa funções importantes de bash
devhelp  # lista os comandos disponiveis
dkbuild  # constroi imagem docker para este projeto
dknpminstall  # instala as dependencias do front-end dentro do container
dkup  # roda o servidor
```

Com o `dkup` rodando, abra outro terminal

```bash
dk bash  # inicia bash dentro do container "picklejar"
./manage.py migrate  # cria as tabelas do banco de dados
./manage.py createsuperuser  # cria superusuario no banco de dados
```

---

Arquitetura baseada em: [evolutio/djvue](https://github.com/evolutio/djavue)