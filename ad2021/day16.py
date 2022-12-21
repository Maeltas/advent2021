lines=open("input16", "r")
def bin2int(text):
    result=0
    bin=1
    for i in range(len(text)):
         result+=int(text[len(text)-i-1])*bin
         bin*=2
    return result

def add_packet(bits,packets,versions):
    version = bits[0:3]
    versions.append(version)
    id = bits[3:6]
    bits2=bits[6:]
    length=6
    if id=="100":
        i=0
        while bits2[i*5]!="0":
            i+=1
        length+=(i+1)*5
        length+=8-length%8
        packets.append(bits[0:length])
    else:
        if bits2[0]=="1":
            how_many=bin2int(bits2[1:12])
            length+=12+how_many*11
            length += 8 - length % 8
            packets.append(bits[0:length])
            for i in range(how_many):
                add_packet(bits2[12+i*11:12+(i+1)*11],packets,versions)
        else:
            how_many = bin2int(bits2[1:16])
            length += 1 + how_many
            length += 8 - length % 8
            packets.append(bits[0:length])
            bits3=bits2[16:]
            i=0
            print(bits3)
            while i<how_many:
                if bits3[3:6]=="100": #literal
                    length=6
                    j = 0
                    while bits3[6+j * 5] != "0":
                        j += 1
                    length += (j + 1) * 5
                    packets.append(bits3[0:length])
                    versions.append(bits3[0:3])
                    bits3=bits3[length:]
                    i+=length
                else:
                    print(bits3)



dict={
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111",
}
input=""
output=""
for x in lines:
    for a in range(len(x)):
        input+=dict[x[a]]

packets=[]
versions=[]
add_packet(input,packets,versions)
print(input)
print(packets)
print(versions)