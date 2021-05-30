# Parcial Final - Lohanna Aguirre
Crear una aplicación que permita procesar y visualizar (Dashboard) el número tweets publicados por hashtags en tiempo real. Los conteos tienen que realizarse en tiempo real utilizando spark-streaming en una instancia de AWSEC2.



## Ejecución

### 1.Se debe cambiar la dirección del ec2 en el html
```
cd .. 
cd ..
cd /var/www/html
sudo nano parcial3.html 
axios.get('http://nuevadireccionEC2:5000/dashboard').then(function(response){
cd 
```
### 2. Activar el entorno virtual
```
source env/bin/activate
```

### 3. Se debe ejecutar el archivo server.py
```
python server.py
```
### 4. Se ejecuta el tweet.py
```
python tweet.py
```

### 5. Se ejecuta el process.py
```
spark-submit  process.py localhost 9898
```
