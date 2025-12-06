#Proyecto Talento Tech - Comisión 252472


## Authors

- [@Pablo Bianchi](https://www.github.com/pablobianchi)


## Documentación
Test automatizado sobre el sitio
[Swag Labs](https://www.saucedemo.com)


## Dependencias

Instalación de dependencias

```bash
  pip install -r requirements.txt
```
    
## Ejecución

Para ejecutar las pruebas

```bash
  pytest -v
```

Si se requiere tener un output en formato HTML

```bash
  pytest --html=reports/report.html --self-contained-html
```

(nota) : cada ejecución genera dentro de la carpeta reports/screenshots los archivos de evidencia de cada caso de prueba