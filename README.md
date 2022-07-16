# Desafio-NewCombin

Se crearon 3 scripts para el desarrollo de este desafio. 
1. Generator.py
2. Menu.py
3. Recibo.py

# Compilacion #

Todos los archivos de python y sqlite3 deben estar en el mismo lugar. En caso se quiera usa una base de datos vacia, borrar las .db existentes y correr el script "Generator.py". Despues correr el script "Menu.py" para poder utilizar las funcionalidades solicitadas. 

# Generator.py #

Es un script para genera una base de datos en SQLite3 para poder manejar y simular deudas de servicios pendientes. La tabla consiste en 4 elementos:
  1. Codigo (ID)
  2. Nombre de Servicio
  3. Fecha de Cobro
  4. Precio

Para usar este script, al momento de compilar, ingresar las 4 areas que se piden y luego para seguir ingresando datos, ingresar 1. En caso de ingresar otro valor despues de ingresar los 4 elementos, se terminara el ingreso de datos. Si se quiere aumentar elementos, volver a compilar.


# Menu.py #

El script principal del desafio, aqui estan todas las funcionalidades proncipales. 
  1. Verificacion de Debito/Credito
  2. Pago con Cash
  3. Historial de Pagos

Para usar este script, compilar y leer los menus.  Este script utiliza el script de Facturacion poara crear una tabla donde se registrara los pagos hechos. Ademas que obtiene los datos de la tabla deuda, donde se mostran todos los servicios pendientes de pago y sus estados. 

Dentro de las funcionalidades, se podra ver todas las deuda o por servicio. Ademas que se paga mediante el ingreso de codigo(ID) del servico. Un vez se realize el pago, se actuiliza la tabla de facturacion y la tabla de deudas. 


