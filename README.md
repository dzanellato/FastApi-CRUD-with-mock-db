# FastAPI_CRUD_without_db

Os end points que devem ser implementados em uma API RESTful são:


| Route Name | URL Path         | HTTP Method | Purpose                                |
|------------|------------------|-------------|----------------------------------------|
| Index      | /object          | GET         | Display list of all objects            |
| New        | /object/new      | GET         | Offers form to create new object       |
| Create     | /object          | POST        | Creates new object on server           |
| Show       | /object/:id      | GET         | Displays one specific object's details |
| Edit       | /object/:id/edit | GET         | Offers form to edit object             |
| Update     | /object/:id      | PUT/PATCH   | Updates specific object on server      |
| Destroy    | /object/:id      | DELETE      | Deletes specific object                |


**Obs.:** *Object* na *URL Path* da tabela acima representa alguma recurso exposto pela API e, por convenção, deve estar no **plural**. 

Aqui criaremos artificialmente uma base de dados que armazena postagens feitas por usuários em alguma rede social ou fórum (obtida de https://jsonplaceholder.typicode.com/posts). Assim, a tarefa da API será mediar o acesso ao "banco de dados" de postagens. Os end points da API serão:


| Route Name | URL Path        | HTTP Method | Purpose                                    |
|------------|-----------------|-------------|--------------------------------------------|
| Index      | /posts          | GET         | Lista todas as postagens                  |
| Create     | /posts          | POST        | Armazena uma nova postagem                 |
| Show       | /posts/:id      | GET         | Retorna a postagem especificada pelo id    |
| Update     | /posts/:id      | PUT/PATCH   | Atualizada a postagem especificada pelo id |
| Destroy    | /posts/:id      | DELETE      | Deleta a postagem especificada pelo id     |


