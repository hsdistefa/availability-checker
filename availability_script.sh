#!/bin/bash

cd "$(dirname "$0")";
curl -s -d "YII_CSRF_TOKEN=535ab25961950109832e8df490d1b6d300224460&OrderItem%5BpreferredDate%5D=2019-10-25&OrderItem%5BminDate%5D=2019-10-18&OrderItem%5Bproduct%5D%5Bid%5D=343915&ItemQuantity%5B343915%5D%5B0%5D%5BpriceOption%5D%5Bid%5D=3545586&ItemQuantity%5B343915%5D%5B0%5D%5Bquantity%5D=1&ItemQuantity%5B343915%5D%5B1%5D%5BpriceOption%5D%5Bid%5D=3545587&OrderItem%5BselectedSessionId%5D=134766371&OrderItem%5BsessionId%5D=134766371" -X POST https://lasafaris.rezdy.com/updateTotalprice | python3 curl_checker.py
