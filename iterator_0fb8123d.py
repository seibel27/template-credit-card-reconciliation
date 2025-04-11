from abstra.tasks import get_trigger_task, send_task

task = get_trigger_task()
payload = task.get_payload()

iterator_list = payload.get("rejected_expenses", [])
if isinstance(iterator_list, list):
    for item in iterator_list:
        dto = task.get_dto()
        payload["expense"] = item
        send_task(dto.type, payload)

task.complete()
