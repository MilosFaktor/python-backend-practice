# utils/util.py


def get_end_time(request_id, start, end, logger):
    exec_time = f"{(end - start):.6f}"
    logger.info(f"Request_id: {request_id} - 'END' - Execution time: {exec_time}")

    return
