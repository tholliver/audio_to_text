# Vosk 
## Instalación y funcionamiento  

Tener instalado ffmpeg 

Ir a: 

https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z

Una vez descargado descomprimir e ingresar al directorio [ffmpeg-5.1.2-full_build.7z] Una vez dentro buscar el directorio [bin], copiamos la ruta para acceder a los binarios:

Ejemplo:

C:\Users\{TuUsuario}\Downloads\ffmpeg-5.1.2-full_build\bin

Video de ayuda (Se omiten los siguientes pasos):
[Editar|Agregar PATH en Windows](https://www.youtube.com/watch?v=eEEp_BSToQ4) 

Ahora abrimos el buscador de Windows escribimos "Variables de entorno" abrimos la primera recomendación. Se abren las [propiedades del sistema] y en la parte inferior están las [Variables de entorno] hacemos click. 

Se despliegan las variable de entorno del usuario actual y del sistema: Hacemos click en [PATH], des mostraran rutas a diferentes binarios ya configurados:
Presionamos en [Nuevo] y pegamos la ruta que se había copiado anteriormente, finalizamos haciendo click en ACEPTAR o OK y 
abrimos el CMD, recomendado abrir uno nuevo para que se lean los nuevos cambios.

Testear ejecutando en cmd:

```bash 
> ffmpeg
```
Se debe desplegar todos los comandos de FFMPEG.

Para la ejecución del programa:

## Ejecución de programa 

Ejecutar:

```bash 
> git clone https://github.com/tholliver/audio_to_text.git
```

```bash 
> cd audio_to_text
```

Primero se necesita un entorno de python para todos los módulos:
``` bash
> conda create -n voskenv python=3.7
```
[voskenv] -- > Es un ejemplo puede tener cualquier nombre. La version de Python sera 3.7.

Una vez terminado el proceso se debe ejecutar (Dentro del DIR del proyecto (audio_to_text)):

```bash 
> conda install --file requirements.txt
```

Terminando el proceso, se puede proceder a ejecutar el programa. 

Nota: Asegurase de tener el entorno activado y estar dentro del directorio del proyecto (audio_to_text): 

Ejemplo: 

```bash
(voskenv) D:\Mis-Proyectos\Boom\audio_to_text>
```

Probar con los audios de ejemplo:

```bash
> python test.py 
```





