# ponderada-04
ponderada 04
As bibliotecas necessárias são importadas, incluindo fastapi, CORSMiddleware, File, UploadFile, Request, Body, FileResponse, StreamingResponse, os, create_client e Client do supabase, YOLO do ultralytics, BaseModel do pydantic, cv2 e base64. Essas bibliotecas são usadas para criar um servidor FastAPI, manipular arquivos, fazer chamadas ao Supabase, realizar detecção de objetos usando YOLO, processar imagens, etc.

O código carrega o modelo YOLO usando o arquivo "best.pt" e lê uma imagem chamada "rachadura.jpg" usando a função cv2.imread().

A aplicação FastAPI é inicializada criando uma instância do FastAPI().

A URL e a chave de autenticação são definidas para se conectar ao Supabase usando a biblioteca supabase e a função create_client().

É adicionado um middleware CORSMiddleware à aplicação FastAPI para lidar com a política de mesmo origem (CORS). Isso permite que outras origens acessem a API.

As variáveis table_name e schema_name são definidas para especificar a tabela e o esquema no Supabase que serão usados para armazenar os dados.

É definida uma classe imagem que herda da classe BaseModel do pydantic. Essa classe representa a estrutura de dados que será usada para validar o corpo da solicitação da rota "/imagem".

É definida uma rota POST chamada "/imagem" usando o decorador @app.post. Essa rota recebe uma solicitação do tipo Request. Dentro da função, é criada uma nova instância do cliente Supabase usando a função create_client().

É aberto um arquivo chamado "runs/detect/predict/image0.jpg" em modo de leitura binária usando open(). O conteúdo do arquivo é lido e convertido em uma string base64 usando a função base64.b64encode(). Essa string é atribuída à variável my_string.

Uma chamada é feita para a função insert() do cliente Supabase, inserindo um novo registro na tabela especificada (table_name) com a coluna "imagem" e o valor my_string. A função execute() é chamada para executar a operação de inserção.

A resposta do Supabase é impressa no console.

A função retorna um dicionário com a mensagem "Image uploaded successfully".

video : https://youtu.be/kESfeOLssj8
