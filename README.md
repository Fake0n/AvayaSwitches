# Avaya Switches / Cisco Switches / Routers / cisco / avaya
Позволяет из файла достать список IP адресов коммутаторов и в каждый прописать заданные команды. Команды нужно прописывать в порядке очереди,
дабы все выполнялось корректно.
В принципе - подойдет для любого сетевого оборудования, у которого есть подключение по SSH.
Возможно, кому-то поможет. Вывод, правда, пока не очень комфортный для чтения, да и подкрутить асинхронность было бы не плохо, чтобы выполнялся код быстрее,
но даже так - существенно быстрее, чем вбивать на большом количестве L2/3 свитчей те же VLANы.
С небольшими поправками подойдет и на свитчи Cisco.
