def my_sort(file, col):
    items=[]
    try:
        with open(file, 'r') as f:
            for line in f:
                record=line.split()
                items.append(record)
    except IOError:
        print(f'cannot open file {file}')
    if 0<col-1< len(items[0]):
        try:
            sorted_rerords=sorted(items, key=lambda x:int(x[col-1]))
            for item in sorted_rerords: 
                for x in item:
                    print(x, end=' ')
                print("")
            # for item in sorted_rerords:
            #     print(' '.join(item))
        except ValueError:
            print(f'cannot sort by column {col} not numeric')
            return
    
    



my_sort('fileA.txt', 3)