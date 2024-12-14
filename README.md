# 🌟 Proyecto: Biblioteca Virtual 🌟

## 📚 Descripción General
La **Biblioteca Virtual** es una aplicación web **Fullstack** diseñada para gestionar una colección de libros y usuarios de manera eficiente. El objetivo principal es ofrecer una solución sencilla y atractiva para el manejo de una biblioteca, integrando funcionalidades modernas tanto en el frontend como en el backend.

---

## 🚀 Objetivos del Proyecto
- **Gestión de libros:** Registro, consulta, edición y eliminación de libros.
- **Control de usuarios:** Registro de usuarios, roles (administrador/lector), y gestión de actividades.
- **Préstamos y devoluciones:** Sistema automatizado para llevar un control detallado de préstamos y fechas límite.
- **Búsqueda avanzada:** Filtrar libros por autor, título, género, disponibilidad, y más.

---

## 🛠️ Tecnologías Utilizadas

### **Frontend**
- **HTML:** Estructura de las páginas web.
- **CSS:** Estilización y diseño visual.
- **JavaScript:** Dinamismo e interactividad.
- **Bootstrap:** Framework para diseño responsivo y moderno.

### **Backend**
- **Python:** Lenguaje de programación principal.
- **FastAPI:** Framework para la creación de APIs rápidas y seguras.
- **MySQL:** Base de datos relacional para almacenar la información.
- **MySQL Workbench:** Herramienta para el diseño y gestión de la base de datos.

---

## 📈 Funcionalidades Principales
1. **Gestión de libros:**
   - CRUD (Crear, Leer, Actualizar, Eliminar) para los libros.
2. **Gestión de usuarios:**
   - Registro y edición de datos personales.
   - Asignación de roles (Administrador,Bibliotecario o Lector).
3. **Control de préstamos:**
   - Registro de préstamos y devoluciones con control de fechas.
4. **Búsqueda y filtros:**
   - Búsqueda avanzada de libros por múltiples criterios.
5. **Interfaz responsiva:**
   - Accesible desde dispositivos móviles, tablets y escritorios.

---

## 🛠️ Instalación y Configuración

### **Requisitos Previos**
- Python 3.10+
- MySQL Workbench

### **Instrucciones de Configuración**
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/edierGuerra/biblioteca-virtual.git
   cd biblioteca-virtual
   ```
2. **Configurar el entorno virtual:** 
   ```bash
   # Desde la carpeta backend
   python -m venv venv
   # En Linux/Mac: source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias:**
   ```bash
   #Desde la carpeta backend
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos:**
   - Crear una base de datos en MySQL Workbench llamada `biblioteca_virtual`.
   - Importar el archivo `backend/schema.sql` (que contendrá el diseño inicial de la base de datos).

5. **Iniciar el servidor FastAPI:**
   ```bash
   uvicorn backend.main:app --reload
   ```

6. **Acceder a la aplicación:**
   - Frontend: [http://localhost:8000](http://localhost:8000)
   - Documentación interactiva de la API: [http://localhost:8000/docs](http://localhost:8000/docs)



## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas contribuir:
1. Realiza un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad o corrección de errores.
3. Envía un Pull Request para revisión.

---

## 📝 Licencia
Este proyecto está bajo la Licencia MIT. Puedes consultarla en el archivo `LICENSE`.

---

## 🌟 Autores
Creado por: **Edier Guerra, Junior Herrera, Camilo Ospina**  
Edier: [LinkedIn](https://www.linkedin.com/in/edier-guerra-404094335/) | [GitHub](https://github.com/edierGuerra)
