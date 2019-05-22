#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def esterilizar():	
	vuelta=0
	print("====running the process for disinfecting hard disks====")
	while vuelta<int(sys.argv[10]):
		porcentaje=vuelta+1
		print("==========Completed "+str(porcentaje)+"/"+sys.argv[10])
		ValorIF="if=/dev/zero"
		ValorOF=" of="+sys.argv[2]
		ValorBS=" bs="+sys.argv[4]
		ValorCount=" count="+sys.argv[6]
		ComandoDDZERO="dd "+ValorIF+ValorOF+ValorBS+ValorCount
		os.system(ComandoDDZERO)
		ValorIF="if=/dev/urandom"
		ValorOF=" of="+sys.argv[2]
		ValorBS=" bs="+sys.argv[4]
		ValorCount=" count="+sys.argv[6]
		ComandoDDRANDOM="dd "+ValorIF+ValorOF+ValorBS+ValorCount
		os.system(ComandoDDRANDOM)
		vuelta=vuelta+1
	print("====End of the disinfection process of hard disks====")
def formatear():
	print("====Formatting====")
	UNMOUNT="umount "+sys.argv[2]
	os.system(UNMOUNT)
	FORMATEAR="sudo mkfs.vfat -F 32 -n "+sys.argv[8]+" "+sys.argv[2]
	os.system(FORMATEAR)
	print("====End...====")
def menu():
	print("================================================MENU=================================================")
	print("| Sintaxis:                                                                                          |")
	print("| python main.py -of Dispositivo -bs tamañoBloque -ct NumeroSectores -n Nombre -v Iteraciones        |")
	print("|                                                                                                    |")
	print("| Dispositivo: Dirección donde esta montada el Dispositivo, df -h para obtenerla                     |")
	print("| tamañoBloque: tamaño de los bloques, fdisk -l 'ruta' para obtenerlo o 512 por defecto              |")
	print("| NumeroSectores: Numero de sectores que tiene el Dispositivo, fdisk -l para obtenerlo               |")
	print("| Nombre: nombre que se le asignara al Dispositivo despues de formatear                              |")
	print("| Iteraciones: Numero de iteraciones para rellenar con ceros y numeros aleatorios el Dispositivo     |")
	print("|====================================================================================================|")
	print("| Ejemplo:                                                                                           |")
	print("| python main.py -of /dev/sdb1 -bs 512 -ct 3446784 -n Mi-USB -v 99                                   |")	
	print("|====================================================================================================|")
	print("| Creado por: Davinson Mellizo                                                                       |")
	print("| Correo: davinsonmellizo@unicauca.edu.co                                                            |")
	print("| Profesor: Siler Amador Donado                                                                      |")
	print("| Fecha: 21/05/2019                                                                                  |")
	print("| Repositorio:                                                                                       |")
	print("=====================================================================================================")
if __name__ == "__main__":
	if sys.argv[1]=="-of" and sys.argv[3]=="-bs" and sys.argv[5]=="-ct" and sys.argv[7]=="-n" and sys.argv[9]=="-v":
		esterilizar()
		formatear()		
	else:
		menu()
		
	
