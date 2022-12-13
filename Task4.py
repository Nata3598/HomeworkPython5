# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def serial_find(line):
    res = []
    count = 0
 
    if len(line) == 1:
        res.append( (1, int( line[0] ) ) )
        return res
 
    for i in range( len(line) ):
        count += 1
        if (i + 1) == len(line) or line[i] != line[i + 1]:
            res.append( (count, line[i]) )
            count = 0

    return res

def zip_cort(cort):
    res = ''
    count = 0
    temp = [0,'']
    for i in range( len(cort) ):
        s = cort[i]
        if s[0]>1:
            if temp[0] != 0:
                res = res + str( temp[0] ) + temp[1]
                temp = [0,'']
            res = res + str( s[0] ) + s[1]
        else: 
            temp = [ temp[0] - s[0], temp[1] + s[1] ]

    if temp[0] != 0:
        res = res + str( temp[0] ) + temp[1]

    return res
            
def zip_file(in_filename, out_filename):
    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            for line in in_file:
                cort = serial_find( line )
                # print( cort )
                string = zip_cort( cort )
                out_file.write( string )
            out_file.close()
        in_file.close()

def unzip_file( in_filename, out_filename ):
    with open( in_filename, 'r') as in_file:
        with open( out_filename, 'w') as out_file:
            res = ''
            
            for line in in_file:
                i = 0

                while i in range( len(line) ):
                    if line[i] == '-': 
                        i+=1
                        res = res + line[ i+1 : i+1 + int( line[i] ) ]
                        i = i + int( line[i] ) + 1
                    
                    elif int( line[i] ) > 1:
                        res = res + line[ i+1 ] * int ( line[i] )
                        i+=2
                # print (res)

            out_file.write(res)
            out_file.close()
        in_file.close()

print( 'Compress input.txt to output_zip.txt' )
zip_file('input.txt', 'output_zip.txt')

print( 'Uncompress output_zip.txt to output_unzip.txt' )
unzip_file('output_zip.txt', 'output_unzip.txt')