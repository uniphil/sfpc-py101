### Input

- embedded in source code

    ```py
    name = 'phil'
    print 'hello ' + name
    ```

- command line arguments

    ```py
    import sys
    name = sys.argv[0]
    print 'hello ' + name
    ```

- pipe/stdin
    - not going to do this because it's annoying

- files

    ```py
    f = open('name.txt')
    name = f.read()
    print 'hello ' + name
    ```

    ```py
    with open('name.txt') as f:
        name = f.read()
    print 'hello ' + name
    ```

- serial
    - pyserial!

- web
    - requests+bs


### Output

- print to stdout
    - `print` done.
    - do this because it's easy!
        - pipe to `say`
        - write to file
        - upload to web
        - send to serial
        - ...

- write to file

    ```py
    with open('out.txt', 'w') as o:
        o.write('stuff to save')
    ```

    - (and all the same things as input, from within python)
