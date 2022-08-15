def removeNine(number):
    '''
    Remove extra NINE in brazil phone numbers from E.164 default numbers
    *Parameter:
        number -> valid phone number E.164
    
    created by @brauner_dev
    '''
  
    default_E164 = number

    print (default_E164)
    print ("Tamanho original:", len(default_E164))

    if (len(default_E164) > 13):
        print ("Prefixo:", default_E164[0:5] )
        converted = default_E164[0:5] + default_E164[6:14]
        print ("Numero novo:", converted)
    else:
        print (default_E164)
      
      
removeNine("+5548991585362")
