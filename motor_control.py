import time
from buildhat import Motor

# Asume que un motor está conectado al puerto A del Build HAT
motor_a = Motor('A')

print("Motor conectado al Puerto A. Preparando para prueba...")

def test_motor():
    """Corre una prueba simple: gira en un sentido y luego en el otro."""
    try:
        print("-> Girando en sentido horario por 2 segundos...")
        motor_a.run_for_seconds(seconds=2, speed=50)
        time.sleep(3) # Espera a que termine el movimiento

        print("-> Girando en sentido anti-horario por 2 segundos...")
        motor_a.run_for_seconds(seconds=2, speed=-50)
        time.sleep(3) # Espera a que termine

        print("Prueba de motor finalizada.")

    except Exception as e:
        print(f"Ocurrió un error durante la prueba: {e}")

if __name__ == "__main__":
    test_motor()

