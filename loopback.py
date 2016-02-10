#!/usr/bin/python

# Idea for this code came after reading the initial post from INE: http://blog.ine.com/2014/05/05/ios-random-ipv4-ipv6-route-generator-in-tcl/
#
__author__ = 'mmaslows'

import random

def loopback_gen():

    i = range(int(raw_input("How many interfaces would you like to generate? >>> ")))

    j = raw_input("Which class subnet mask should we use? -options: a, b, c, all >>> ")
    while j not in ['a', 'b', 'c', 'all']:
        j = raw_input("Which class subnet mask should we use? -options: a, b, c, all >>> ")

    masks_A = ('128.0.0.0', '192.0.0.0', '224.0.0.0', '240.0.0.0', '248.0.0.0', '252.0.0.0', '254.0.0.0', '255.0.0.0')
    masks_B = ('255.128.0.0', '255.192.0.0', '255.224.0.0', '255.240.0.0', '255.248.0.0', '255.252.0.0', '255.254.0.0', '255.255.0.0')
    masks_C = ('255.255.128.0', '255.255.192.0', '255.255.224.0', '255.255.240.0', '255.255.248.0', '255.255.252.0', '255.255.254.0', '255.255.255.0')
    masks_D = ('255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240', '255.255.255.248', '255.255.255.252', '255.255.255.254', '255.255.255.255')

    if j == 'a':
          masks = masks_A
    elif j == 'b':
          masks = masks_B
    elif j == 'c':
          masks = masks_C
    elif j == 'all':
          masks = masks_A + masks_B + masks_C + masks_D
    else:
        print "Improper option provided"



    loopback_num = 10000

    print "\n\n"
    print "%20s %20s %20s %20s %20s %20s %20s" % ("IP_Address", "Subnet_Mask", "First_Octet_Binary", "Second_Octet_Binary", "Third_Octet_Binary", "Fourth_Octet_Binary",  "Bit_Count",)

    for number in i:
          a = (random.randrange(1,223))
          b = (random.randrange(1,255))
          c = (random.randrange(1,255))
          d = (random.randrange(1,255))

          x = (random.choice(masks))
          z = str(a) + "." + str(b) + "." + str(c) + "." + str(d)

          mask_octets = x.split(".")
          first_octet_bin = bin(int(mask_octets[0]))
          second_octet_bin = bin(int(mask_octets[1]))
          third_octet_bin = bin(int(mask_octets[2]))
          fourth_octet_bin = bin(int(mask_octets[3]))

          y1 = first_octet_bin
          y2 = second_octet_bin
          y3 = third_octet_bin
          y4 = fourth_octet_bin

          print "\n"
          print "interface loopback"+(str(loopback_num+number))
          print "ip address " + str(a) + "." + str(b) + "." + str(c) + "." + str(d) + " " + x

if __name__ == '__main__':
    loopback_gen()
