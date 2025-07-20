# Controlador de Motores con Raspberry Pi y Build HAT

Un proyecto simple de Python para controlar motores LEGO Technic usando la placa Build HAT en una Raspberry Pi.

## Requisitos

- Raspberry Pi con la Build HAT conectada.
- Un motor LEGO Technic (conectable a la Build HAT).
- Python 3.

## Instalación

1.  **Clona este repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO_EN_GITHUB>
    cd rpi_buildhat_controller
    ```

2.  **Instala las dependencias:**
    (La librería `buildhat` ya debería estar instalada en tu sistema. Este archivo es una buena práctica para futuros usos con entornos virtuales).
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1.  Conecta un motor LEGO al **Puerto A** de la Build HAT.
2.  Ejecuta el script de prueba:
    ```bash
    python3 motor_control.py
    ```

El script hará girar el motor en un sentido y luego en el otro para verificar que todo funciona correctamente.
