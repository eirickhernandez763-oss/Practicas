def RoundRobin(Procesos: list[dict], Quantum: int) -> None:
    """Simula Round Robin e imprime el tiempo de espera por proceso."""

    Cola = [{"nombre": P["nombre"], "restante": P["burst"]} for P in Procesos]
    Tiempo = 0
    Espera = {P["nombre"]: 0 for P in Procesos}

    print(f"Quantum = {Quantum} ms\n{'-' * 40}")

    while Cola:
        Actual = Cola.pop(0)

        Turno = min(Quantum, Actual["restante"])
        Sobra = Actual["restante"] - Turno

        print(f"t={Tiempo}ms — {Actual['nombre']} correrá {Turno}ms "
              f"(restante: {Actual['restante']} → {Sobra})")

        # aumentar espera de los demás procesos
        for Esperando in Cola:
            Espera[Esperando["nombre"]] += Turno

        Tiempo += Turno
        Actual["restante"] -= Turno

        if Actual["restante"] > 0:
            Cola.append(Actual)
        else:
            print(f"  t={Tiempo}ms — {Actual['nombre']} TERMINÓ")

    Promedio = sum(Espera.values()) / len(Espera)

    print(f"\n{'=' * 40}")
    print("Proceso   Espera")
    print('-' * 40)

    for Nombre, TiempoEspera in Espera.items():
        print(f"{Nombre}        {TiempoEspera} ms")

    print(f"{'-' * 40}")
    print(f"Promedio     {Promedio:.1f} ms")


if __name__ == "__main__":

    Procesos = [
        {"nombre": "P1", "burst": 8},
        {"nombre": "P2", "burst": 3},
        {"nombre": "P3", "burst": 2},
    ]

    print("ESCENARIO 1 — Quantum pequeño (q=2)")
    print("=" * 40)
    RoundRobin(
        [{"nombre": P["nombre"], "burst": P["burst"]} for P in Procesos],
        Quantum=2
    )

    print("\nESCENARIO 2 — Quantum grande (q=10)")
    print("=" * 40)
    RoundRobin(
        [{"nombre": P["nombre"], "burst": P["burst"]} for P in Procesos],
        Quantum=10
    )