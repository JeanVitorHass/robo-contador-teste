import random
import time

from pantheon.athena.sdk import sdk

TOTAL_ITENS = 40
TAXA_FALHA = 0.1  # ~10% dos itens falham, para o KPI ter algo a mostrar


def processar(item_id: int) -> None:
    """Simulate processing one item. Raises on the simulated failures."""
    time.sleep(random.uniform(0.15, 0.4))
    if random.random() < TAXA_FALHA:
        raise RuntimeError(f"Conta {item_id} nao fechou (divergencia simulada)")


def main() -> None:
    print("Iniciando robo de contagem...")
    sdk.log.info(f"Robo iniciado — {TOTAL_ITENS} contas na fila")

    for item_id in range(1, TOTAL_ITENS + 1):
        try:
            processar(item_id)
            sdk.kpi.add_success(current_item=item_id)
            sdk.log.info(f"Conta {item_id} processada com sucesso")
            print(f"Conta {item_id}: OK")
        except Exception as exc:
            sdk.kpi.add_failure(current_item=item_id)
            sdk.log.error(str(exc), item_id=item_id)
            print(f"Conta {item_id}: FALHOU — {exc}")
        finally:
            sdk.kpi.report()

    print(f"Robo finalizado — {sdk.kpi.success} ok, {sdk.kpi.failed} falharam.")
    sdk.execution.finish()


if __name__ == "__main__":
    main()
