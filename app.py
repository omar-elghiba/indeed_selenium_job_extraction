import pandas as pd
from concurrent.futures import as_completed, ThreadPoolExecutor
from extract_data import extract_data






def new_extract_all_data_pro(job_number=100, proxies=None, num_threads=10, proxy_pages_limit=2, jobs_per_page=15):
    if proxies is None:
        proxies = ['proxy_1','proxy_2','proxy_3','proxy_4','proxy_5','proxy_6']

    page_number = -(-job_number // jobs_per_page)  
    pages_per_thread = -(-page_number // num_threads) 


    page_ranges = [range(i*pages_per_thread, min((i+1)*pages_per_thread, page_number)) for i in range(num_threads)]

    dfs = []

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_df = {executor.submit(extract_data, page_range, proxies[i%len(proxies)], proxy_pages_limit): i for i, page_range in enumerate(page_ranges)}
        for future in as_completed(future_to_df):
            dfs.append(future.result())

    return dfs