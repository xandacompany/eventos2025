# Documentación del Proyecto

## Descripción

Este es un sitio web desarrollado y diseñado por **Asiel Jiménez** para la empresa **Mundo Ejecutivo**, con el objetivo de mostrar los eventos programados para el año 2025. En este sitio se pueden encontrar detalles sobre eventos importantes como **Cumbre 200**, **TI**, **Mundo Sustentable**, **Fintech** y **Cumbre 1000**.

**Ruta del proyecto:**  
[https://grupomundoejecutivo.com/eventos2025/index](https://grupomundoejecutivo.com/eventos2025/index)

## Estructura del Proyecto

El proyecto sigue una estructura sencilla para su organización. A continuación se describen las carpetas y archivos principales:

### Raíz del Proyecto

- `assets/`: Contiene todos los archivos esenciales del proyecto.
  - `styles/`: Archivos de estilos CSS.
    - `main.css`: Archivo principal de estilos para el sitio.
  - `images/`: Contiene las imágenes utilizadas en el sitio web.
  - `json/`: Archivos JSON que pueden ser utilizados para almacenar información dinámica o configuraciones.
    - `package.json`: Archivo de configuración del proyecto.
  - `scripts/`: Contiene los scripts JavaScript utilizados en el sitio.
    - `main.js`: Archivo principal de JavaScript que maneja la interactividad del sitio.

- `config/`: Carpeta que contiene archivos de configuración.
  - `sistem.py`: Script encargado de cargar todos los archivos dentro de la carpeta `docs` al archivo `sistemap.xml`.

- `docs/`: Contiene la documentación o archivos que el sistema necesita para ser procesados por `sistem.py`.

### Funcionamiento de `sistem.py`

El archivo `sistem.py`, ubicado en la carpeta `config`, tiene la función de cargar automáticamente todos los archivos contenidos en la carpeta `docs` al archivo `sistemap.xml`. Este proceso es esencial para la correcta administración y visualización de los eventos dentro del sitio web.

## Instalación

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/xandacompany/eventos2025.git
    ```

2. **Instala las dependencias**:
    Si el proyecto tiene dependencias JavaScript, como se indica en el archivo `package.json`, puedes instalar las dependencias con el siguiente comando:
    ```bash
    npm install
    ```

3. **Configuración del entorno**:
    Asegúrate de que el archivo `sistem.py` pueda acceder a los archivos dentro de la carpeta `docs` para generar el archivo `sistemap.xml` correctamente.

4. **Lanza el servidor o abre el archivo `index`**:
    Si el proyecto requiere un servidor local, puedes utilizar herramientas como **Live Server** en VSCode o configuraciones locales de Node.js, o simplemente abrir el archivo `index.html` directamente en tu navegador.

## Funcionalidades

- **Página principal**: Muestra la lista de eventos programados por Mundo Ejecutivo para 2025.
- **Interactividad**: El sitio permite la navegación fluida entre los diferentes eventos.
- **Diseño responsive**: El diseño es adaptable a diferentes tamaños de pantalla, optimizado para dispositivos móviles.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama con tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios y haz un commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Empuja los cambios a tu repositorio (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request para revisar y fusionar tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
