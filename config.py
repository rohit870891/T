import os
import logging
import re
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

my_cookie = os.environ.get("PANWEB=1;browserid=DbGhIfUwCmz5pRL9tNJXj71VLCdZrMpJCpPmKGukZJeoKTWs9RGbALdghHUX9LKmR2YNgbW3uYThf_Qx; lang=en; TSID=fe2VGbjvZZ8mG6VoBnSOKa9tzuKhVwfm; __bid_n=194d786a6d8a0663344207; _ga=GA1.1.1902279557.1738782858; _gcl_au=1.1.955760083.1738782878; _fbp=fb.1.1738782878094.854442062512751170; _ga_RSNVN63CM3=GS1.1.1738782878.1.0.1738782882.56.0.0; csrfToken=rrRaANB6emff_Cw1hA9R3JY5; __stripe_mid=7ed47557-32aa-4096-ba79-c391f754e8b547445a")
my_headers = os.environ.get("")
session_string = os.environ.get("BQFW2cgAYlyhcCV5p6F7c0r_15EhmooKo-e9wRNcoPfnVxYIA6XCHwxB7iQt4x_HgPza-CzEja_Y1TCC7zdg9lqFnFWBQcHV6FStzHkrUGjdsIeoxw9T0LN_NnRAyuqMtOCrbNgl5GVhdrvhzjLLwrkaBlNGh9MVWl7Ysc2jMjsxvyAMTYejWJrG07IiPOiu2uUB-VQ7YeVmqGXWYvYMgmHG0_j82DMRWC9KJblkIp3GGIe07FPBrP_Dlj2-PIhBCCrqsX8daYdKMByoQUCQccdJj_kXs17w_v5lEh6pbs5px4kCLCRfSapFsS_vcm90isJ4DhKcn9I6HOtKvEedU7-1j2hCwgAAAAG00gEJAA")
allowed_groups = os.environ.get("-1002170811388") # added random group id to avoid NoneType error
# allowed_groups = ["-123232ZCVZB"] or ["121222xxx", "123456xxx"]
owner_id = os.environ.get("7328629001")

try:
    my_cookie = eval(my_cookie)
    my_headers = eval(my_headers)
    allowed_groups = eval(allowed_groups)
except Exception as e:
    logger.error(f"Error parsing env variables: {e}")


def extract_links(message):
    # fetch all links
    try:
        url_pattern = r'https?://\S+'
        matches = re.findall(url_pattern, message)

        return matches
    except Exception as e:
        logger.error(f"Error extracting links: {e}")
        return []
