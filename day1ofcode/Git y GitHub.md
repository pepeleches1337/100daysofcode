# Git y GitHub

Generar un repositorio vacío en nuestro directorio actual
`git init`

El comando previo, nos crea dos ficheros que monitorizan los archivos que se van modificando a lo largo del tiempo:
* index.js
* package.json

Si borramos el directorio oculto **.git** borramos Git de nuestro proyecto.
`rm -rf .git`

**GitLens** es un plugin para VSCode que nos proporciona información útil y nos da un panel con el historial de Git.

**.gitignore** nos permite especifica los archivos a ignorar. Por ej., para mantener fuera cualquier API Key privada, logs innecesarios, etc.
`touch .gitignore`

Para la creación de .gitignore existen plugins que te generan toda la estructura directamente.

Un commit es como una página en un libro de historia que tiene su propio ID único y no se puede cambiar sin que Git lo sepa.

Con `git add .` agregamos el directorio actual entero. También, podemos añadir archivos concretos.

Existen dos tipos de estados:
* Staged
* Unstaged

En VSCode es muy fácil variar estos estados.

Si queremos dejar el directorio actual en Unstaged podemos hacer `git reset .`

Si se pone `git reset . --hard` se deja el directorio actual en Unstaged y **se BORRA PARA SIEMPRE**, obligando a empezar de nuevo.

Tip: **Hacer muchos pequeños commits** porque no solo ayudará a evitar pérdidas catastróficas de código, sino que también hará que los cambios de código sean mucho más fáciles de seguir.

```
git commit -m "mensaje descriptivo
sobre lo que cambiamos
en nuestro código"
```

PD: Usar Emojis en el mensaje descriptivo para obtener más Stars.
* Primeras línea -> Resumen
* Segunda línea -> Conjunto descriptivo de cambios 

Git nos mostrará los cambios realizados.

Con GitLens podemos verificar el historial para ver las líneas que se han modificado.

`git branch` ver ramas actuales

Hasta ahora, hemos trabajado con lo que se denomina la rama **master**, que es como el tronco principal del árbol que contiene el código fuente que se va a entregar a los clientes.

### ¿Qué sucede cuando tienes un código estable y necesitas corregir un error o quieres experimentar con una nueva función?

Se debe crear una nueva rama basada en el commit más reciente y corregir el error en una rama separada y luego volver a fusionarla en la rama master una vez que esté lista.

Permite tener varios desarrolladores trabajando en sus propias ramas sin pisarse unos a otros.

`git checkout -b feature` cambiar entre branches (ramas), con -b indicamos que se cree la rama en caso de no existir.

`git branch` para verificar que la rama ha cambiado. Cualquier código que escribamos aquí estará aislado en esta rama.

No es necesario hacer un commit de los archivos antes de cambiar a la rama master.

Si está trabajando en algo que está a medio terminar o es experimental, puede usar un comando llamado `git stash`. Esto guardará los cambios actuales sin tener que hacer un commit y luego volver a un directorio limpio.

`git stash pop`

Reservar los cambios actuales para usarlos en algún momento posterior.

### Cómo hacer un merge de a la master branch
1. Ir a la master branch
2. Lanzar `git merge feature`

Combinará el último commit de feature en master.

El ID será el mismo para feature que para master.

Al hacer merge pueden ocurrir conflictos. En VSCode aparacerán formas de solucionar estos problemas.

Los small commits nos ayudan a resolver conflictos porque es más sencillo arreglar un archivo que cientos de archivos.

`git merge feature --squash`

### Pushear un repo a GitHub (remotamente)

1. Crear un repositorio en GitHub
2. Nos dará los comandos para pushear nuestro código

El primer comando es `git remote` que conecta nuestro código local con el repositorio remoto.

`git push` pusheará los archivos al repositorio remoto.

3. Ya estará el código disponible en GitHub.

### Fork
Copia el código fuente de otra persona en un repo propio. Se usa para colaborar.

Después, se puede lanzar un `git clone` para editar localmente.

Un Pull Request es como un Merge.

## Referencias
[Git It? How to use Git and Github](https://youtu.be/HkdAHXoRtos)

