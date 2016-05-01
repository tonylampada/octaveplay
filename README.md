Projeto pra brincar de octave.

Instala o docker e builda a imagem com `./build.sh` (vai tomar um cafe)

Entra na imagem com `docker run octaveplay /bin/bash`

Roda o python e roda o exemplo do oct2py:

```
>>> oc = oct2py.Oct2Py()
>>> x = oc.zeros(3,3)
>>> print(x, x.dtype)
[[ 0.  0.  0.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]] float64
...
```

Now let's try to predict some function like 3x²/y - 17xy + 8/z + 0w - 13

octave run.oct