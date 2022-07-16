# Desafío-NewCombin #

Se crearon 3 scripts para el desarrollo de este desafío.
  1. Generator.py
  2. Menu.py
  3. Recibo.py

# Compilación #

Todos los archivos de python y sqlite3 deben estar en el mismo lugar. En caso se quiera usar una base de datos vacía, borrar las .db existentes y correr el script "Generator.py". Después correr el script "Menu.py" para poder utilizar las funcionalidades solicitadas.

# Generator.py #

Es un script para generar una base de datos en SQLite3 para poder manejar y simular deudas de servicios pendientes. La tabla consiste en 4 elementos:
  1. Código (ID)
  2. Nombre de Servicio
  3. Fecha de Cobro
  4. Precio
Para usar este script, al momento de compilar, ingresar las 4 áreas que se piden y luego para seguir ingresando datos, ingresar 1. En caso de ingresar otro valor después de ingresar los 4 elementos, se terminará el ingreso de datos. Si se quiere aumentar elementos, volver a compilar.

# Menu.py #

El script principal del desafío, aquí están todas las funcionalidades principales.
  1. Verificación de Débito/Crédito
  2. Pago con Cash
  3. Historial de Pagos

Para usar este script, compilar y leer los menús. Este script utiliza el script de Facturación para crear una tabla donde se registran los pagos hechos. Además que obtiene los datos de la tabla deuda, donde se muestran todos los servicios pendientes de pago y sus estados.

Dentro de las funcionalidades, se podrá ver todas las deudas o por servicio. Además que se paga mediante el ingreso de código(ID) del servicio. Una vez se realice el pago, se actualiza la tabla de facturación y la tabla de deudas.
