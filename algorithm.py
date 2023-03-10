
#Order Block — средняя цена крупного грока.
#Условие для отрисовки бычьего ОБ:
    #цена должна остановиться после снижения цены — образование последней медвежьей свечи
    #цена должна начать повышение — образование бычьей вечи следом за медвежьей
    #Бычья свеча должна поглотить медвежью

#1. Выгрузка свечей(timeframe-n?) не менее 3х за указанный период(period-n? <= 3)

#2. Если трэнд нисходящий то переход на проверку бычьего ОБ(БОБ)
  #2.1. Если цена остановилась после снижения цены(образование последней медвежьей свечи)
    #2.1.1 Если цена начала повышение(образование бычьей свечи следом за медвежьей)
      #2.1.2 Если бычья свеча поглотила медвежью(бычья больше медвежьей)
        #2.1.2.1 Определить границы БОБ
          #2.1.2.1.1 Взять L последней и следующей свечи Lnext,Llast. Взять H последней и следующей свечи Hnext,Hlast.
          #2.1.2.1.2 Если Lnext больше Llat то взять Lnext
          #2.1.2.1.3 Иначе взять Llast и взять Hlast (Llast, Lnext - нижняя граница блока, Hlast - верхняя граница блока)
        #2.1.2.2 Запуск функции БОБ

#3. Если трэнд восходящий то переход на проверку медвежьего ОБ(МОБ)
  #3.1. Если цена остановилась после повышения цены(образование последней бычьей свечи)
    #3.1.1 Если цена начала понижение(образование медвежьей свечи следом за бычьей)
      #3.1.2 Если медвежья свеча поглотила бычью(медвежья больше бычьей)
        #3.1.2.1 Определить границы МОБ
          #3.1.2.1.1 Взять H последней и следующей свечи Hnext,Hlast. Взять L последней и следующей свечи Lnext,Llast.
          #3.1.2.1.2 Если Hnext больше Hlast то взять Hnext
          #3.1.2.1.3 Иначе взять Hlast и взять Llast. (Hlast, Hnext - верхняя граница блока, Llast -  нижняя граница блока)
        #3.1.2.2 Запуск функции МОБ

