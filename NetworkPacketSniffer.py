#Author : ShafqatHassan
#Dated : 1st; of Mar 2023
#Repo : Shafqathassan/Cyber-Sec_Tools
#HelpFrom : TheNewBoston/YoutubeChannel


#Sockets and the socket API are used to send messages across a network. 
import socket

#Struct module performs conversions between Python values and C structs represented as Python bytes objects.
import struct

#Textwrap module can be used for wrapping and formatting of plain text. 
import textwrap


#these are just gonna format out text and more readable and attractive
TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t '
DATA_TAB_1 = '\t\t ' 
DATA_TAB_1 = '\t\t\t ' 
DATA_TAB_1 = '\t\t\t\t ' 



def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    #The AF_PACKET socket in Linux allows an application to receive and send raw packets.
    #Once an application creates a socket of type SOCK_RAW, this socket may be used to send and receive data. 
    #socket. ntohs captures all the send & receive traffic from the network interface.
    
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print("\nEthernet frame: ")
        print(TAB_1 + 'Destination: {}, source: {}, proto: {}'.format(dest_mac, src, eth_proto))

        
        #8 for IPv4 
        if eth_proto == 8:
            (version, header_length, ttl, proto, srfc, target, data) =ipv4_packet(data)            
            print(TAB_1 + 'ipV4 packet: ')
            print(TAB_2 + 'Version : {}, Header Length: {}, TTL: {}'.format(version, header_length, ttl))    
            print(TAB_3 + 'Protocol : {}, Source: {}, Target: {}'.format(proto, src, target))    


            #1 for TCMP 
            if  proto ==1:
                icmp_type, code, checksum, data = icmp_packet(data)
                print(TAB_1 + 'ICMP Packet: ')
                print(TAB_2 + 'Type : {}, Code: {}, Checksum: {}'.format(version, header_length, ttl))    
                print(TAB_2 + 'Data:'.format(proto, src, target))    
                print(format_multiline(DATA_TAB_3, data))


            # 6 for TCP
            elif proto ==6:
                (version, header_length, ttl, proto, srfc, target, data) =ipv4_packet(data)            
                print(TAB_1 + 'TCP Segment: ')
                print(TAB_2 + 'Source Port : {}, Destination Port: {}'.format(src_port, dest_port))    
                print(TAB_2 + 'Sequence : {}, Acknowldgment: {}'.format(sequence, acknowledgment))
                print(TAB_2 + 'Flags: ')
                print(TAB_3 + 'URG : {}, ACK: {} PSH : {}, RST : {} SYN : {}, FIN : {}'.format(flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin))
                print(TAB_2 + 'Data: ')
                print(format_multiline(DATA_TAB_3, data))


            #17 for UDP
            elif proto ==17:
                src_port, dest_port, Length, data = udp_segment(data)
                print(TAB_1 + 'UDP Segment: ')
                print(TAB_2 + 'Source Port : {}, Destination Port: {}, Length'.format(src_port, dest_port, Length))    
                
            #Other (mainly we use TCP , UDP)
            else:
                print(TAB_1 + 'Data: ')
                print(format_multiline(DATA_TAB_2, data))


        else:
            print('Data: ')
            print(format_multiline(DATA_TAB_1, data))            
                
            


# Unpack ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac) , get_mac_addr(src_mac), socket.htons(proto), data[14:]

#Return properly formatted MAC Address (ie AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format(), bytes_addr)
    return ':'.join(bytes_str).upper()


# Unpack IPv4 packet
def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl , proto , src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]


# Returns properly formatted IPv4 address
def ipv4(addr):
    return '.'.join(map(str, addr))


# Unpack ICMP packet
def icmp_packet(data):
    icmp_type, code, checksum = strict.unpcak('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

#  Unpack ICMP packet
def tcp_segment(data):
    (src_port, dest_port, sequence, acknowledgment, offset_reserved_flags)= struct.unpack('! H H L L H',data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, sequence, acknowledgment, flag_ack, flag_fin, flag_psh, flag_rst, flag_syn, flag_urg, data[offset:]


#  Unpack UDP segment
def udp_segment(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, data[8:]


#Format multi-line data
def format_multiline(prefix, string, size=80):
    size= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])



main()
