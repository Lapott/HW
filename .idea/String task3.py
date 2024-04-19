output = b"\r\nHuawei Versatile Routing Platform Software\r\nVRP (R) software, Version 8.220 (CE6857EI V200R022C00SPC500)\r\nCopyright (C) 2012-2022 Huawei Technologies Co., Ltd.\r\nHUAWEI CE6857-48S6CQ-EI uptime is 248 days, 3 hours, 14 minutes\r\n"
arr = output.decode('utf-8')
print (arr)
spl_arr = arr.replace('\r' , "")
print (spl_arr)
spl_arr1 = spl_arr.lstrip()
print (spl_arr1)

