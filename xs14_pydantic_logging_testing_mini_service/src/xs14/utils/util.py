# utils/util.py


def get_end_time(request_id, start, end, logger):
    duration = f"{(end - start):.6f}"
    logger.info(f"Request_id: {request_id} - 'END' - Execution time: {duration}\n")

    return
