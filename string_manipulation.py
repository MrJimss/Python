data = "14inch l@ptop,699|16inch l@ptop,999|sm@rtphone,1099|t@blet,499|g@ming pc,1999"
data=data.replace("@","a")
device_list = data.split("|")
formatted_list=[]
for device in device_list:
  device_info_list = device.split(",")
  name = device_info_list[0]
  price = int(device_info_list[1])
  price=int(price+(price*0.1))
  device=(f"Device: {name}", f"${price}")
  formatted_list.append(device)
for device in formatted_list:
  print(device)

