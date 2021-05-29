# Parcial Final - Lohanna Aguirre
Crear una aplicación que permita procesar y visualizar (Dashboard) el número tweets publicados por hashtags en tiempo real. Los conteos tienen que realizarse en tiempo real utilizando spark-streaming en una instancia de AWSEC2.



## Ejecución
### 1. Se debe ejecutar el archivo server.py
```
python server.py
```
### 2. Se ejecuta el tweet.py
```
python tweet.py
```

### 2. Se ejecuta el process.py
```
spark-submit  process.py localhost 9898
```
