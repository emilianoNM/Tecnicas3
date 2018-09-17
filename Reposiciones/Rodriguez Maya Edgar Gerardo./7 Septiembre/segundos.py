###segundos a horas minutos y segundos

num=int(input("ingrese los segundos\n"))
hor=(int(num/3600))
minu=int((num-(hor*3600))/60)
seg=num-((hor*3600)+(minu*60))
print str(hor)+"h "+str(minu)+"m "+str(seg)+"s"