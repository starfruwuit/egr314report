---
title: API
--- 
## Message Type - Motor Speed
|     | data type | variable name | smallest number recognized | largest number recognized | example of valid data |
|-----|-----------|---------------|----------------------------|---------------------------|-----------------------|
| Bytes 1-2 | char | prefix | n/a | n/a | b'AZ |
| Byte 3 | char | sender | n/a | n/a | b'B' |
| Byte 4 | char | receiver | n/a | n/a | b'G' |
| Bytes 5-x | char | motorSpeed | 0 | 150 | 130 |
| Bytes x+1 to x+2 | char | suffix | n/a | n/a | b'YB' |

## Message Type - Motor Safety
|     | data type | variable name | smallest number recognized | largest number recognized | example of valid data |
|-----|-----------|---------------|----------------------------|---------------------------|-----------------------|
| Bytes 1-2 | char | prefix | n/a | n/a | b'AZ' |
| Byte 3 | char | sender | n/a | n/a | b'S' |
| Byte 4 | char | receiver | n/a | n/a | b'G' |
| Byte 5 | char | safety | 0 | 1 | 1 |
| Bytes 6-7 | char | suffix | n/a | n/a | b'YB' |

# Message Type - Feedback
|     | data type | variable name | smallest number recognized | largest number recognized | example of valid data |
|-----|-----------|---------------|----------------------------|---------------------------|-----------------------|
| Bytes 1-2 | char | prefix | n/a | n/a | b'AZ |
| Byte 3 | char | sender | n/a | n/a | b'G' |
| Byte 4 | char | receiver | n/a | n/a | b'H' |
| Bytes 5-x | char | feedback | n/a | n/a | "hello world" |
| Bytes x+1 to x+2 | char | suffix | n/a | n/a | b'YB' |