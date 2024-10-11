curl -L --insecure -x 172.30.71.80:3128 -X POST 'http://172.30.71.10:50510/api/v2/oauth' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Accept: application/json' \
-H 'RqUID: 6f0b1291-c7f3-43c6-bb2e-9f3efb2dc98e' \
-H 'Authorization: Basic OGJiZTg3NGEtNjA0OS00NjQ3LTk1YWMtNzVhNDNjNzdmODUxOjU0MTY1OWNhLWI3NDctNDBlZS05MTM3LWY3Y2M0OGY3NWQ4Zg==' \
--data-urlencode 'scope=GIGACHAT_API_CORP'


curl -L --insecure -x 172.30.71.80:3128 -X POST 'http://172.30.71.10:50511/api/v1/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: 'eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.cwblYRMT-YBS_NyKCvnYqWsGAq-fduAagQWLChUXf5hYm8FtqmgFoILKu0dyckClP-6EfgJ16vVw7i8KKMMIeOO5mXUDcnZFSEE0zkvH0w4-NW_sCvIprpwCd2-zY--NRPlEO-2O9hp8N_HLbgP7agv0BNFVHGAzsrY8fOW5uzHdBsyGfj9tosG1j9rKpMHjGkbLLQsOjMj8zz0PEm70U23rgL31s8L1qyY7j8td2gipbmeOPFvJmQyeV6PYIYEA2EuGkeOr7fmwYI7EVGfG1oRwSEc6_43eAxgm_rlAlkFYRoBVdvyi8MLkrbsxR-d1PfNX8Wi3YIBgzw9Dvlg9Cg.b41UfUSrrnMHUtZoLGIBBw.yq7Qytw1WJeltRujbTc1OcbhjK6yWUic9Majq8NWi673LAqG5UStBs2EKU9zBYQvcGMRDnOXTEEoMahzTdaHgjlPw7xe-IjY4TR3FfkMPpx631eYnHs6TOVBn_ErvxQA5bXxceI4j7THdqnTgIJ3RO5x-ob02ZWtprcOYFJcH36MpkFpKvs77IOM-WBhSDikV-ZsHqdOxRefyZCFw566bsWUIp_PbWPNF-3DQJNsHuRN75c2yEER79OxFlyV5HAPRByK_a2wiI30GRTViZA2AvvL1p-u5VRT_GTJstYqBn95N2njFl3IRwXOHyJi447W01oq4pTT3IxZif9Z_RclWeRl27h5-hmgtpfL7MNu4Jq7n6Ob33pObCyrvtWZN3cpSNf6Cwa10zjmso-pchw2QXZZtOFKOh29Q_FjFimSVBdYpA0vo85aDR7HeVNxGHtSD9cSgTk7PQatCL0UgTygwhsdG1VX600_lJ8RL8sRQ3tcXxfA39hQ9UHoxGrku076v5v03-ZHoOxJije0rn8EbGOJUkZTA1t3N3HANGSw1hIrcwirke7o2cSGaIz6ZUWidzariPlYpTueHuHwj3IUCxGiS_EJRc68EDRk5Yp_Su7IfRho8TwEFCz38M-3EzwcT5V88o3LODUsL4oKXtprYmaHRB74Wialr_J3xbKtGWWgt6UKE4XqhGEWdd-sIx-qkjpOWC4FrfTDujys6J9_ifrUsBDn_VAuaKc6LDX59b4.ij-4mfJkMBgAopyjALgIW1si37M9NCjLy5a_BCIlWAg' \
--data-raw '{
  "model": "GigaChat",
  "messages": [
    {
      "role": "system",
      "content": "Ты опытный специалит контакт-центра Банка"
    },
    {
      "role": "user",
      "content": " 12082024 14082024 "
    }
  ],
  "temperature":1,
  "top_p":0.1,
  "n": 1,
  "stream": false,
  "max_tokens":100,
  "update_interval": 0
}'
