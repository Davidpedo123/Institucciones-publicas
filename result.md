![[Pasted image 20241210190417.png]]
el de abajo es sin optimizar la db con docker

Sin docker
![[Pasted image 20241210190757.png]]
Luego de aplicar el #PRAGMA y la #Concurrencia a la base de datos
![[Pasted image 20241210202824.png]]
#TercerPaso para mejorar el rendimiento, en este caso, #reciclamos los datos, envitamos llamar nuevamente a datos estaticos que antes ya teniamos
![[Pasted image 20241210205628.png]]
#Cache-cliente
Como la api sera lo mas ligera utilizaremos cache, pero departe del cliente, este solo sera notable, de parte si solicita desde un navegador
![[Pasted image 20241210212408.png]]
#todo-async aqui tanto el dump, el config y el main lo convertimos totalmente async ![[Pasted image 20241210220007.png]]


#Comandos
#docker build -t api-inst -f ./deployment/Dockerfile .
#docker run -p 8080:8080 -h "0.0.0.0" api-inst