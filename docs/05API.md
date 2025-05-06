---
title: API
--- 
## Message Type 6 - Motor Speed
|     | data type | variable name | smallest number recognized | largest number recognized | example of valid data |
|-----|-----------|---------------|----------------------------|---------------------------|-----------------------|
| Byte 1-2 | char | prefix | n/a | n/a | b'AZ |
| Bytes 5 | char | motorSpeed | 0 | 150 | 130 |

## Message Type 3 - Motor Safety
|     | data type | variable name | smallest number recognized | largest number recognized | example of valid data |
|-----|-----------|---------------|----------------------------|---------------------------|-----------------------|
| Byte 1 | uint8_t | motorSpeed | 0 | 150 | 130 |
