# hateProject
Hate(Hamster)  Projecto para hacer mas comoda la estadia del conejo de mi Hija.
fin de semana 12-dic se añade control de un relevador para activar un foco de 40w que calienta la jaula a ciertas horas del dia para aumentar la temperatura de la jaula




Añadir estas lineas en crontab
usando crontab -e 


0 5 * * * sudo python /home/pi/releLuz.py&
0 7 * * * sudo python /home/pi/releLuz.py&
0 20 * * * sudo python /home/pi/releLuz.py&
0 22 * * * sudo python /home/pi/releLuz.py&
59 23 * * * sudo python /home/pi/releLuz.py&
