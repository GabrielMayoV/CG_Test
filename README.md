# CG_Test
# Backend Challenge from Common Gound

Hola! Soy Gabriel Mayo y este es mi repositorio del challenge para Backend.

Traté de hacer lo mejor posible dentro del límite de tiempo, ahora listaré las funcionalidades implementadas y las que quedaron pendientes.

## Funcionalidades:
* API con Django.
* GET y POST en los enpoints .../api/products/ y .../api/products/bulk_insert respectivamente.
* Deployment a un Elastic Beanstalk de AWS.
* Conexión a una base de datos de postgreSQL.
* Carga a un repositorio público.

### Uso:

**Método POST para insertar datos**
```
curl --location --request POST 'http://django-env.eba-vx9jtvag.us-west-2.elasticbeanstalk.com/api/products/bulk_insert/' \
--header 'Content-Type: application/json' \
--data-raw '{"name":NAME,
"value":VALUE,
"discount_value":DISCOUNT,
"stock":STOCK}'
```

**Método GET para consulta de productos**

`curl --location --request GET 'http://django-env.eba-vx9jtvag.us-west-2.elasticbeanstalk.com/api/products/'`


## Funcionalidades no implementadas:
* Validaciones de los datos de entrada: los datos no pasan por las validaciones solicitadas, en caso de tener más tiempo se implementaría una validación por el método clean() de Django.

Quedo al pendiente por cualquier cosa y espero les guste mi trabajo.

Saludos!
