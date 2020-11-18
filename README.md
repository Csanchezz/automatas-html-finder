# Cognito integrado en AppSync

Este es un ejemplo simple para conectar cognito con appsync de una manera automatizada para agilizar el mantenimiento por medio del framework ```serverless```

## Para Empezar

Las siguientes instrucciones serviran si se quiere hacer deployment del mismo ejemplo de la "api" en tu cuenta de ```AWS```, **Nota:** esto tambien puede funcionar localmente.

### Prerequisitos

  1. Python3.6
  2. AWS-CLI (instalado y configurado solo para hacer deploy en aws [click aquí](https://docs.aws.amazon.com/es_es/polly/latest/dg/setup-aws-cli.html))
  3. Serverless Framework ( de igual manera solamente para deploy en aws [instalación](https://www.serverless.com/framework/docs/providers/aws/guide/installation/))
  4. Virtualenv (este es requerido [instalación](https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/)) 


### Deployment

Básicamente debemos instalar los `node_modules` y los paquetes de `python`

Paso #1

```
npm install
```

Paso #2

```
pip install -r requirements.txt (dentro del entorno virtual(virtualenv))
```


Paso #3
```
sls deploy (en caso de que lo quiera subir a aws)
```

aparecerá algo parecido al siguiente bloque

```
$ sls deploy
AppSync Plugin: GraphQl schema valid
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service sls-appsync-backend.zip file to S3 (#.## MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
................
Serverless: Stack update finished...
Service Information
service: nombre-de-tu-servicio
stage: stage-de-tu-servicio
region: region-de-tu-servicio
stack: nombre-de-tu-servicio-stage
resources: ##
api keys:
  None
appsync api keys:
  None
endpoints:
  None
appsync endpoints:
  https://url-de-tu-servicio-apigateway.region.amazonaws.com/nombre-funcion
functions:
  nombre-funcion: nombre-servicio-stage-funcion
layers:
  None
Serverless: Removing old service artifacts from S3...
```

Ahora podes manualmente a tu api en appsync y loguearte por medio de algun usuario (previamente creado en cognito) y realizar las queries, mutations en la API.

